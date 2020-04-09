from django.shortcuts import render
from rest_framework import status, viewsets
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.models import User
from user.serializer import UserSerializer


@api_view(['GET'])
def login(request):
    if request.method == 'GET':
        email = request.GET.get("email")
        password = request.GET.get("password")
        user = User.objects.filter(email=email, password=password)
        return Response(data=UserSerializer(user, many=True).data, status=status.HTTP_200_OK)




class signup(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#
#
# @api_view(['POST'])
# def signup(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         name = request.POST.get('name')
#
#         user = User(email=email, password=password, address=address, phone=phone, name=name)
#         user.save()
#         return Response(data=UserSerializer(user, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
def info(request):
    if request.method == 'GET':
        info = Information.objects.all()
        return Response(data=InfoSerializer(info, many=True).data, status=status.HTTP_200_OK)
