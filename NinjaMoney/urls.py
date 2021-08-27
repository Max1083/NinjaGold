from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('process_money',views.process_money,name='process_money'),
]