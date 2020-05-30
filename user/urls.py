from django.conf.urls import url
from django.urls import include
from rest_framework.routers import SimpleRouter

from user.views import *

router = SimpleRouter()

router.register('products', AllProductView, 'ProductView')
router.register('user', UserViewset, 'order')
router.register('post', PostView, 'PostView')
router.register('media', MediaView, 'PostView')
router.register('category', CategoryViewset, 'PostView')



urlpatterns = [
    # url('', include(router.urls), name='router'),
    url(r'^login', login, name='login'),
    url(r'^upload/', simple_upload, name='old'),
    url(r'^makepost/', make_post, name='old'),
    url(r'^makesell/', make_sell, name='old'),
    url(r'^makecomment/', add_comment, name='old'),
    url(r'^addlike/', add_like, name='old'),
    # url(r'^signup', signup, name='signup'),
    # url(r'^info', info, name='about'),
    url(r'^api/', include(router.urls), name='api'),
]
