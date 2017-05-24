from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.select, name='select'),            #Select Page
    url(r'^results/$', views.results, name='results'),  #Results Page
    url(r'^submit/$', views.submit, name='submit'),     #Used to submit selection
    url(r'^refresh/$', views.refresh, name='refresh'),  #Used for ajax updates
]