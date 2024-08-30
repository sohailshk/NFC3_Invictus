from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.volunteer_form, name='volunteer_form'),
    path('list/', views.volunteer_list, name='volunteer_list'),
    path('', views.index, name='index'),
]
