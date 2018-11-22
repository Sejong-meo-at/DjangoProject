from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="main"),
    url(r'^blog/new/$', views.new, name="new"),
    url(r'^blog/detail/(?P<pk>\d+)/$', views.detail, name="detail"),
    url(r'^blog/delete/(?P<pk>\d+)/$', views.delete, name="delete"),
    url(r'^blog/update/(?P<pk>\d+)/$', views.update, name="update"),
]
