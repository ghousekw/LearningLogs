from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<list_id>', views.edit, name='edit'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('strike_off/<list_id>', views.strike_off, name='strike_off'),
    path('unstrike/<list_id>', views.unstrike, name='unstrike'),
]