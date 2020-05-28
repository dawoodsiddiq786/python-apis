from rest_framework import serializers
from user.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    posted_by = UserSerializer(many=False)

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    posted_by = UserSerializer(many=False)
    likes = UserSerializer(many=True)
    comments = CommentSerializer(many=True)
    media=MediaSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'



class PostSkinnySerializer(serializers.ModelSerializer):


    class Meta:
        model = Post
        fields = '__all__'

