# Register your models here.
from django.contrib import admin

from chat.models import ThreadList, Messages

admin.site.register([ThreadList, Messages])
