from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/?$', views.signupform, name='signup'),
    url(r'^signupcomplete/?$', views.signupcomplete, name='signupcomplete'),
    ]
