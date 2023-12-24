from pyramid.view import view_config, view_defaults

from rest_api.grpc.client import SepatuClient

import traceback

import rest_api.grpc.sepatu_pb2 as sepatu_pb2


@view_config(route_name="sepatus", renderer="json")
def sepatuss_view(request):
    try:
        client = SepatuClient()

        sepatus = client.get_sepatus()

        return sepatus
    except Exception as e:
        request.response.status = 500
        return dict(
            status="error",
            message=str(e),
        )


@view_config(route_name="sepatus", renderer="json", request_method="POST")
def create_sepatu_view(request):
    try:
        if (
            request.json_body is None
            or "name" not in request.json_body
            or "description" not in request.json_body
            or "price" not in request.json_body
            or "image_url" not in request.json_body
            or "stock" not in request.json_body
        ):
            request.response.status = 400
            return dict(
                status="error",
                message="Bad request",
            )

        client = SepatuClient()

        sepatu = client.create_sepatu(
            sepatu=sepatu_pb2.Sepatu(
                name=request.json_body["name"],
                description=request.json_body["description"],
                price=request.json_body["price"],
                image_url=request.json_body["image_url"],
                stock=request.json_body["stock"],
            )
        )

        if "error" in sepatu:
            request.response.status = 400
            return dict(
                status="error",
                message=sepatu["error"]["message"],
            )

        return sepatu
    except Exception as e:
        print(traceback.format_exc())

        request.response.status = 500
        return dict(
            status="error",
            message=str(e),
        )


@view_config(route_name="sepatu", renderer="json", request_method="PUT")
def update_sepatu_view(request):
    try:
        if (
            request.json_body is None
            or "name" not in request.json_body
            or "description" not in request.json_body
            or "price" not in request.json_body
            or "image_url" not in request.json_body
            or "stock" not in request.json_body
        ):
            request.response.status = 400
            return dict(
                status="error",
                message="Bad request",
            )

        client = SepatuClient()

        sepatu = client.update_sepatu(
            sepatu=sepatu_pb2.Sepatu(
                id=int(request.matchdict["id"]),
                name=request.json_body["name"],
                description=request.json_body["description"],
                price=request.json_body["price"],
                image_url=request.json_body["image_url"],
                stock=request.json_body["stock"],
            )
        )

        if "error" in sepatu:
            request.response.status = 400
            return dict(
                status="error",
                message=sepatu["error"]["message"],
            )

        return sepatu
    except Exception as e:
        request.response.status = 500
        return dict(
            status="error",
            message=str(e),
        )


@view_config(route_name="sepatu", renderer="json", request_method="DELETE")
def delete_sepatu_view(request):
    try:
        client = SepatuClient()

        sepatu = client.delete_sepatu(int(request.matchdict["id"]))

        if "error" in sepatu:
            request.response.status = 404
            return dict(
                status="error",
                message=sepatu["error"]["message"],
            )

        return sepatu
    except Exception as e:
        request.response.status = 500
        return dict(
            status="error",
            message=str(e),
        )


@view_config(route_name="sepatu", renderer="json")
def sepatu_view(request):
    try:
        client = SepatuClient()

        sepatu = client.get_sepatu(int(request.matchdict["id"]))

        if "error" in sepatu:
            request.response.status = 404
            return dict(
                status="error",
                message=sepatu["error"]["message"],
            )

        return sepatu
    except Exception as e:
        request.response.status = 500
        return dict(
            status="error",
            message=str(e),
        )
