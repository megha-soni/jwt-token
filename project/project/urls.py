from django.contrib import admin
from app1.views import *
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',RegisterAPI.as_view()),
    path('login/',LoginAPI.as_view()),
    path('verify/',OTPverify.as_view())
]
