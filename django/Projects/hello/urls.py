from django.urls import path
from . import views

urlpatterns = [
    path('say_hello/', views.say_hello, name='index'),
    path('home/',views.home),
    path('get_method/',views.method, name='method'),
    path('getuser/<name>/<id>', views.pathview, name='pathview'),
    path('getuser/', views.query, name='getuser'),
    path('showform/', views.showform, name='showform'),
    path('showform/getform/', views.getform, name='getform'),
    path('drink/<str:name>',views.getdrink, name='drink')
]