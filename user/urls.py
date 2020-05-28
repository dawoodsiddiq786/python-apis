from django.conf.urls import url
from django.urls import include
from rest_framework.routers import SimpleRouter

from user.views import login, UserViewset, ProductView, simple_upload, PostView, MediaView, PostViewCreate, make_post

router = SimpleRouter()

router.register('ProductView', ProductView, 'ProductView')
router.register('user', UserViewset, 'order')
router.register('post', PostView, 'PostView')
router.register('media', MediaView, 'PostView')




urlpatterns = [
    # url('', include(router.urls), name='router'),
    url(r'^login', login, name='login'),
    url(r'^upload/', simple_upload, name='old'),
    url(r'^makepost/', make_post, name='old'),

    # url(r'^signup', signup, name='signup'),
    # url(r'^info', info, name='about'),
    url(r'^api/', include(router.urls), name='api'),
]
