from concurrent import futures
import time
import logging
import grpc

import traceback

import sepatu_pb2
import sepatu_pb2_grpc

from sepatu import Sepatu
from sqlalchemy import create_engine, insert, text, values, select, update, delete, desc


engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/utsbagus")


class SepatuService(sepatu_pb2_grpc.SepatuServiceServicer):
    def List(self, request, context):
        try:
            with engine.connect() as conn:
                sepatus = conn.execute(select(Sepatu)).all()

                return sepatu_pb2.SepatuListResponse(
                    sepatus=[
                        sepatu_pb2.Sepatu(
                            id=sepatu.id,
                            name=sepatu.name,
                            description=sepatu.description,
                            price=sepatu.price,
                            image_url=sepatu.image_url,
                            stock=sepatu.stock,
                        )
                        for sepatu in sepatus
                    ]
                )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
            return sepatu_pb2.SepatuListResponse()

    def Create(self, request, context):
        try:
            with engine.connect() as conn:
                conn.execute(
                    insert(Sepatu),
                    [
                        {
                            "name": request.name,
                            "description": request.description,
                            "price": request.price,
                            "image_url": request.image_url,
                            "stock": request.stock,
                        }
                    ],
                )

                conn.commit()

                return sepatu_pb2.SepatuCreateResponse(
                    sepatu=sepatu_pb2.Sepatu(
                        name=request.name,
                        description=request.description,
                        price=request.price,
                        image_url=request.image_url,
                        stock=request.stock,
                    )
                )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
            return sepatu_pb2.SepatuCreateResponse()

    def Get(self, request, context):
        try:
            with engine.connect() as conn:
                sepatu = conn.execute(
                    select(Sepatu).where(Sepatu.id == request.id)
                ).first()

                if sepatu is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    context.set_details("sepatu not found")
                    return sepatu_pb2.SepatuResponse()

                return sepatu_pb2.SepatuResponse(
                    sepatu=sepatu_pb2.Sepatu(
                        id=sepatu.id,
                        name=sepatu.name,
                        description=sepatu.description,
                        price=sepatu.price,
                        image_url=sepatu.image_url,
                        stock=sepatu.stock,
                    )
                )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
            return sepatu_pb2.sepatuResponse()

    def Update(self, request, context):
        try:
            with engine.connect() as conn:
                conn.execute(
                    update(Sepatu)
                    .where(Sepatu.id == request.id)
                    .values(
                        name=request.name,
                        description=request.description,
                        price=request.price,
                        image_url=request.image_url,
                        stock=request.stock,
                    )
                )

                conn.commit()

                return sepatu_pb2.SepatuUpdateResponse(
                    sepatu=sepatu_pb2.Sepatu(
                        name=request.name,
                        description=request.description,
                        price=request.price,
                        image_url=request.image_url,
                        stock=request.stock,
                    )
                )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
            return sepatu_pb2.SepatuUpdateResponse()

    def Delete(self, request, context):
        try:
            with engine.connect() as conn:
                conn.execute(delete(Sepatu).where(Sepatu.id == request.id))

                conn.commit()

                return sepatu_pb2.SepatuDeleteResponse(
                    message="sepatu deleted successfully"
                )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
            return sepatu_pb2.SepatuDeleteResponse()


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sepatu_pb2_grpc.add_SepatuServiceServicer_to_server(SepatuService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started at port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    server()
