from django.db import models
from django.utils import timezone
from user.models import User
from user.models import Product


class ThreadList(models.Model):
    reciever = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='reciever_id',  # Here
                                    db_column='reciever_id')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, default=None, null=True)
    timestamp = models.DateTimeField(default=timezone.now)


class Messages(models.Model):
    thread = models.ForeignKey(ThreadList, on_delete=models.CASCADE, default=None)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    is_seen = models.BooleanField(default=False, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
