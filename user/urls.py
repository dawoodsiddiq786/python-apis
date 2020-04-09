from django.conf.urls import url
from django.urls import include
from rest_framework.routers import SimpleRouter

from user.views import login, signup, info

router = SimpleRouter()


router.register('signup', signup, 'order')

urlpatterns = [
    # url('', include(router.urls), name='router'),
    url(r'^login', login, name='login'),
    url(r'^signup', signup, name='signup'),
    url(r'^info', info, name='about'),
    url(r'^api/', include(router.urls), name='api'),
]
