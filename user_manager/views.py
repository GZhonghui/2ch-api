from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model

from .serializers import RegisterLoginSerializer


User = get_user_model()


@api_view(["POST"])
def register(request):
    # if request.method == "POST":
    serializer = RegisterLoginSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # 触发create
        return Response({"success": 1}, status=status.HTTP_200_OK)
    except ValidationError as e:
        error_msg = e.detail.get("username", ["unknown error"])[0]
        return Response(
            {"success": 0, "message": error_msg}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
def login(request):
    serializer = RegisterLoginSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        # TODO: Token
        return Response({"success": 1}, status=status.HTTP_200_OK)
    except ValidationError as e:
        error_msg = ""
        return Response(
            {"success": 0, "message": error_msg}, status=status.HTTP_400_BAD_REQUEST
        )
