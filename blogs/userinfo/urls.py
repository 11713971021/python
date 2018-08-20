from django.conf.urls import url
from .views import *
# 主路由分发的路由，

urlpatterns = [
    url(r'^login/', login_views, name='login'),
    url(r'^register/', register_views, name='regis'),
    url(r'^imgs_code/', imgs_views, name='imgs')

]
