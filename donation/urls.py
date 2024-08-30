from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_donation, name='create_donation'),
    path('list/', views.donation_list, name='donation_list'),
    path('donate/',views.donate_view,name='donate_page'),
]