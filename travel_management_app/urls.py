# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Add other URL patterns as needed
    path("login/",views.user_login),
    path("success/",views.success),
    path("signup/",views.signup,name='signup'),
   
]
