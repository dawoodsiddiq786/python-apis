import json

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


@api_view(['POST'])
def make_post(request):
    if request.method == 'POST':
        description = request.POST.get("description")
        posted_by = request.POST.get("posted_by")
        media = request.POST.get("media")
        post = Post(description=description, posted_by_id=posted_by)
        post.save()
        for m in json.loads(media):
            post.media.add(m)
        post.save()
        return Response(data=PostSerializer(post, many=False).data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_comment(request):
    if request.method == 'POST':
        description = request.POST.get("comment")
        user_id = request.POST.get("user_id")
        post_id = request.POST.get("post_id")
        usr = User.objects.get(id=user_id)
        cmnt = Comment(description=description, posted_by=usr)
        cmnt.save()
        pst = Post.objects.get(id=post_id)
        pst.comments.add(cmnt)
        pst.save()
        return Response(data=PostSerializer(pst, many=False).data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_like(request):
    if request.method == 'POST':
        user_id = request.POST.get("user_id")
        post_id = request.POST.get("post_id")
        usr = User.objects.get(id=user_id)
        pst = Post.objects.get(id=post_id)
        if usr in pst.likes.all():
            pst.likes.remove(usr)
        else:
            pst.likes.add(usr)
        pst.save()
        return Response(data=PostSerializer(pst, many=False).data, status=status.HTTP_200_OK)


@api_view(['POST'])
def make_sell(request):
    if request.method == 'POST':

        description = request.POST.get("description")
        posted_by = request.POST.get("posted_by")
        category = request.POST.get("category")
        price = request.POST.get("price")
        name = request.POST.get("name")
        media = request.POST.get("media")
        cat = Categorie.objects.get(id=category)

        post = Product(description=description, posted_by_id=posted_by, category=cat, name=name, price=price)
        post.save()
        for m in json.loads(media):
            post.media.add(m)
        post.save()
        return Response(data=ProductSerializerAll(post, many=False).data, status=status.HTTP_200_OK)


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostViewCreate(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSkinnySerializer


class MediaView(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class AllProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerAll


class AllProductPatch(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerSkinny
class CategoryViewset(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = Categoryerializer


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
