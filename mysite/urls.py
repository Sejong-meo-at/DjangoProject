from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from blog import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^accounts/signup/$', views.signup, name = 'signup'),
    url(r'^accounts/signup_done/$', views.signup_done, name = 'signup_done'),
]
