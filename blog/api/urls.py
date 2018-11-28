from django.conf.urls import url
from .views import PostListAPIView, PostDetailAPIView, PostUpdateAPIView, PostDeleteAPIView, PostCreateAPIView

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name="api-list"),
    url(r'^new/$', PostCreateAPIView.as_view(), name="api-new"),
    url(r'^detail/(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name="api-detail"),
    url(r'^update/(?P<pk>\d+)/$', PostUpdateAPIView.as_view(), name="api-update"),
    url(r'^delete/(?P<pk>\d+)/$', PostDeleteAPIView.as_view(), name="api-delete"),
]
