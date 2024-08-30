from django.urls import path
from . import views

urlpatterns = [
   path('update_all/', views.update_all_resources, name='resource_update_all'),
   path('update_success/', views.update_success, name='resource_update_success'),  # New URL pattern
   path('create/', views.createresource, name='creation'),
]
