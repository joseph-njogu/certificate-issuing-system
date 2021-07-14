from django.conf.urls import url
from . import views
from . import models
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # url(r'^$', views.login_redirect, name='login_redirect'),
    url('^$',views.index, name='index'),
    url(r'^studentdetails/$', views.studentdetails, name='studentdetails'),
    url(r'^studentslist/$', views.studentslist, name='studentslist'),
]