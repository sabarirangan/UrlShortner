from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<p>[a-z0-9A-Z]{7})',views.redirectfun,name='redirectfun'),
    url(r'^$', views.home,name='home'),

]