from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name ='index'),
    url(r'reset/$', views.reset, name = 'reset'),
    url(r'rps_post/$', views.rps_post, name = 'rps_post')
]
