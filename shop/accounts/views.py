from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import status

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.utils import json
from rest_framework.views import APIView

from .models import CustomUser
from .serializers import ProfileSerializer


class UserLoginView(APIView):
    def get(self, request: Request):
        return render(request, "frontend/signIn.html")

    def post(self, request: Request):
        data = json.loads(request.body)
        user = authenticate(request, username=data['username'],
                            password=data['password'])
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    def post(self, request: Request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserRegisterView(APIView):
    def post(self, request: Request):
        data = json.loads(request.body)
        try:
            user = CustomUser.objects.create_user(username=data['username'],
                                                  password=data['password'],
                                                  first_name=data['name'])
            login(request, user)
            return Response(status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    serializer_class = ProfileSerializer

    def get(self, request: Request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = self.serializer_class(request.user, data=request.data,
                                           partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserAvatarView(APIView):
    def post(self, request: Request):
        user = CustomUser.objects.filter(username=request.user).first()
        user.src = request.FILES['avatar']
        user.alt = 'User avatar image'
        user.save()
        return Response(status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    def post(self, request: Request):
        user = CustomUser.objects.filter(username=request.user).first()
        new_password = request.data["newPassword"]
        cur_password = request.data["currentPassword"]
        check_password = user.check_password(cur_password)
        if check_password:
            user.set_password(new_password)
            user.save()
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
