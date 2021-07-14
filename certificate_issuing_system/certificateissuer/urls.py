from django.conf.urls import url
from . import views
from . import models
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # url(r'^$', views.login_redirect, name='login_redirect'),
    url('^$',views.index, name='index'),
    url(r'^student/$', views.student, name='student'),
    url(r'^students/$', views.StudentList.as_view(), name='StudentList')
]