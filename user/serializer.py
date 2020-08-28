from rest_framework import serializers
from user.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductSerializerSkinny(serializers.ModelSerializer):
    class Meta:
        model = Product
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


    class Meta:
        model = Post
        fields = '__all__'


class PostSkinnySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class Categoryerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


class ProductSerializerAll(serializers.ModelSerializer):
    posted_by = UserSerializer(many=False)
    category = Categoryerializer(many=False)

    ordered_by = UserSerializer(many=False)

    class Meta:
        model = Product
        fields = '__all__'
