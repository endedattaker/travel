# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("packages/",views.packages),
    path("booking/",views.booking),

   
]
