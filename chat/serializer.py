from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from chat.models import ThreadList, Messages
from user.serializer import *


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'


class ThreadSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    reciever = UserSerializer()
    product=ProductSerializerAll()

    class Meta:
        model = ThreadList
        fields = '__all__'
