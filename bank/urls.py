from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.views.generic import RedirectView

urlpatterns = [

     url(r'^$', RedirectView.as_view(url='home')),
     path('home', views.home, name="Home Page"),
     path('addBlood', views.addBlood, name="Add Blood Page"),
     path('delDonor/<int:id>', views.delDonor, name="Del Blood Donor"),
     path('logout', views.handleLogout, name="Logout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)