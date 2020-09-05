import sys
from io import BytesIO

import boto
from PIL import Image
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.crypto import get_random_string
from rest_framework import status, viewsets
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


@api_view(['POST'])
def make_post(request):
    if request.method == 'POST':
        description = request.POST.get("description")
        posted_by = request.POST.get("posted_by")
        media = request.POST.get("media")
        post = Post.objects.create(description=description, posted_by_id=posted_by, media=media)
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
        reason_for_selling = request.POST.get("reason_for_selling")
        address = request.POST.get("address")
        volume = request.POST.get("volume")
        model = request.POST.get("model")
        brand = request.POST.get("brand")
        cat = Categorie.objects.get(id=category)

        post = Product.objects.create(model=model, brand=brand, volume=volume, address=address,
                                      reason_for_selling=reason_for_selling,
                                      description=description, posted_by_id=posted_by, category=cat, name=name,
                                      price=price,
                                      media=str(media))

        return Response(data=ProductSerializerAll(post, many=False).data, status=status.HTTP_200_OK)


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostViewCreate(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSkinnySerializer


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
        raw_image = request.FILES['file']

        im = Image.open(raw_image)
        im = im.convert("RGBA")
        output = BytesIO()

        # Resize/modify the image
        # im = im.resize((300, 100))
        im.thumbnail((300, 300), Image.ANTIALIAS)
        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=90)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        raw_image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % raw_image.name.split('.')[0], 'image/jpeg',
                                         sys.getsizeof(output), None)

        AWS_ACCESS_KEY_ID = 'AKIAXWX2LQE6XYTZIPY6'
        AWS_SECRET_ACCESS_KEY = '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'
        AWS_STORAGE_BUCKET_NAME = 'hueys-list'

        conn = boto.s3.connect_to_region('ap-southeast-2',
                                         aws_access_key_id=AWS_ACCESS_KEY_ID,
                                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                         is_secure=True,  # uncomment if you are not using ssl
                                         calling_format=boto.s3.connection.OrdinaryCallingFormat(),
                                         )

        bucket = conn.get_bucket(AWS_STORAGE_BUCKET_NAME)

        # go through each version of the file

        # create a key to keep track of our file in the storage

        k = Key(bucket)
        k.key = get_random_string(length=10) + raw_image.name.replace(' ', '')

        k.set_contents_from_file(raw_image)

        # we need to make it public so it can be accessed publicly

        # using a URL like http://s3.amazonaws.com/bucket_name/key

        k.make_public()
        url = 'https://hueys-list.s3-ap-southeast-2.amazonaws.com/' + k.key
        return Response({'url': str(url)},
                        status=status.HTTP_201_CREATED)
