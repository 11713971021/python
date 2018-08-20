from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^index', index_views, name='index'),
    url(r'^delete', delete_views, name='deletes'),
    url(r'^write', write_views, name='writes'),
    url(r'^page', page_views, name='page'),

]
