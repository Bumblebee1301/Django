from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from nstrace import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name = 'home'),
    url(r'^details/(\d+)/', views.details, name = 'details'),
    ]
