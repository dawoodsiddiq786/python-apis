from django.db.models import Q
from fcm_django.models import FCMDevice
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from chat.helpers import get_user_id
from chat.models import ThreadList, Messages
from chat.serializer import  *



class ThreadListAll(viewsets.ModelViewSet):
    queryset = ThreadList.objects.all()
    serializer_class = ThreadSerializer

@api_view(['GET'])
def get_all_messages(request):
    if request.method == 'GET':
        sender = request.GET.get("sender")
        receiver = request.GET.get("receiver")
        product = request.GET.get("product", None)
        print(receiver)
        print(sender)
        print(product)
        thread = ThreadList.objects.filter(Q(sender_id=int(sender)) | Q(reciever_id=int(sender)),
                                           Q(sender_id=int(receiver)) | Q(reciever_id=int(receiver)),
                                           product_id=int(product))

        if thread.exists():
            thread = thread[0]
        else:
            thread = ThreadList(
                sender_id=int(sender), reciever_id=int(receiver), product_id=int(product)
            )
            thread.save()

        messages = Messages.objects.filter(thread_id__exact=thread.id)

        if messages.count() > 0:

            return Response(data=MessagesSerializer(messages, many=True).data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"msg": "Messages not found"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def send_messages(request):
    if request.method == 'POST':
        sender = request.POST.get("sender")
        receiver = request.POST.get("receiver")
        text = request.POST.get("text")
        image = request.POST.get("image", None)
        product = request.POST.get("product", None)
        print(receiver)
        print(sender)
        print(product)
        thread = ThreadList.objects.filter(Q(sender_id=int(sender)) | Q(reciever_id=int(sender)),
                                           Q(sender_id=int(receiver)) | Q(reciever_id=int(receiver)),
                                           product_id=int(product))

        if thread.exists():
            thread = thread[0]
        else:
            thread = ThreadList(
                sender_id=int(sender), reciever_id=int(receiver), product_id=int(product)
            )
            thread.save()

        Messages(
            thread_id=thread.id, sender_id=sender,
            text=text, image=image
        ).save()

        # send_notification(text, thread.reciever_id)

        messages = Messages.objects.filter(thread_id__exact=thread.id)

        if messages.count() > 0:
            return Response(data={'':''},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"msg": "Messages not found"}, status=status.HTTP_204_NO_CONTENT)

#
# def send_notification(msg, user):
#     if user.fire_token is not None:
#         device = FCMDevice(
#             id=1,
#             user_id=user.id,
#             registration_id=user.fire_token,
#         )
#         device.send_message(title='Huey\'s List', body=msg, tag='1')
