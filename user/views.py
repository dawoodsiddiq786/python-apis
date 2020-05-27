from django.shortcuts import render
from rest_framework import status, viewsets
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core.files.storage import FileSystemStorage

from user.models import *
from user.serializer import *


@api_view(['GET'])
def login(request):
    if request.method == 'GET':
        email = request.GET.get("email")
        password = request.GET.get("password")
        user = User.objects.filter(email=email, password=password)
        return Response(data=UserSerializer(user, many=True).data, status=status.HTTP_200_OK)


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['POST'])
def simple_upload(request):
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        return Response({'url': 'http://18.217.127.10:9001' + uploaded_file_url}, status=status.HTTP_201_CREATED)
    return Response({'result': 'Only Post Requ'}, status=status.HTTP_401_UNAUTHORIZED)



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

#
# @api_view(['GET'])
# def info(request):
#     if request.method == 'GET':
#         info = Information.objects.all()
#         return Response(data=InfoSerializer(info, many=True).data, status=status.HTTP_200_OK)
