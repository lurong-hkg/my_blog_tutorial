from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.register, name='register'),
    url(r'^(?P<num>\d+)/$', views.detail, name='detail'),
    url(r'^test/$', views.test, name='test'),
    url(r'^home/$', views.home, name='home'),
]