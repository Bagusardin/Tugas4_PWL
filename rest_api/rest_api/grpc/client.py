import grpc

import rest_api.grpc.sepatu_pb2 as sepatu_pb2
import rest_api.grpc.sepatu_pb2_grpc as sepatu_pb2_grpc


class SepatuClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50051")
        self.stub = sepatu_pb2_grpc.SepatuServiceStub(self.channel)

    def get_sepatus(self):
        try:
            response = self.stub.List(sepatu_pb2.SepatuListRequest())
            return [
                {
                    "id": sepatu.id,
                    "name": sepatu.name,
                    "description": sepatu.description,
                    "price": sepatu.price,
                    "image_url": sepatu.image_url,
                    "stock": sepatu.stock,
                }
                for sepatu in response.sepatus
            ]

        except grpc.RpcError as e:
            print(e.details())
            return dict(
                error=dict(
                    code=e.code(),
                    message=e.details(),
                    details=e.debug_error_string(),
                )
            )

    def create_sepatu(self, sepatu):
        try:
            response = self.stub.Create(
                sepatu_pb2.SepatuCreateRequest(
                    name=sepatu.name,
                    description=sepatu.description,
                    price=sepatu.price,
                    image_url=sepatu.image_url,
                    stock=sepatu.stock,
                )
            )

            return dict(
                name=response.sepatu.name,
                description=response.sepatu.description,
                price=response.sepatu.price,
                image_url=response.sepatu.image_url,
                stock=response.sepatu.stock,
            )
        except grpc.RpcError as e:
            print(e.details())
            return dict(
                error=dict(
                    code=e.code(),
                    message=e.details(),
                    details=e.debug_error_string(),
                )
            )

    def get_sepatu(self, id):
        try:
            response = self.stub.Get(sepatu_pb2.SepatuRequest(id=id))

            return dict(
                id=response.sepatu.id,
                name=response.sepatu.name,
                description=response.sepatu.description,
                price=response.sepatu.price,
                image_url=response.sepatu.image_url,
                stock=response.sepatu.stock,
            )
        except grpc.RpcError as e:
            print(e.details())
            return dict(
                error=dict(
                    code=e.code(),
                    message=e.details(),
                    details=e.debug_error_string(),
                )
            )

    def update_sepatu(self, sepatu):
        try:
            response = self.stub.Update(
                sepatu_pb2.SepatuUpdateRequest(
                    id=sepatu.id,
                    name=sepatu.name,
                    description=sepatu.description,
                    price=sepatu.price,
                    image_url=sepatu.image_url,
                    stock=sepatu.stock,
                )
            )

            return dict(
                name=response.sepatu.name,
                description=response.sepatu.description,
                price=response.sepatu.price,
                image_url=response.sepatu.image_url,
                stock=response.sepatu.stock,
            )
        except grpc.RpcError as e:
            print(e.details())
            return dict(
                error=dict(
                    code=e.code(),
                    message=e.details(),
                    details=e.debug_error_string(),
                )
            )

    def delete_sepatu(self, id):
        try:
            response = self.stub.Delete(sepatu_pb2.SepatuDeleteRequest(id=id))

            return dict(
                message=response.message,
            )
        except grpc.RpcError as e:
            print(e.details())
            return dict(
                error=dict(
                    code=e.code(),
                    message=e.details(),
                    details=e.debug_error_string(),
                )
            )
