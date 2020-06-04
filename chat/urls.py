from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from chat.views import *
router = SimpleRouter()

router.register('threads', ThreadListAll, 'threads')

urlpatterns = [
    url(r'^api/', include(router.urls), name='router'),
    url(r'^chat/', include(router.urls), name='chat'),
    url(r'^messages/', get_all_messages, name='messages'),
    url(r'^send/', send_messages, name='send'),

]
