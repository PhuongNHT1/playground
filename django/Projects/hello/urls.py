from django.urls import path
from . import views

urlpatterns = [
    path('say_hello/', views.say_hello, name='index'),
    path('home/',views.home),
]