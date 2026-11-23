from django.urls import path
from . import views

urlpatterns = [

    path('', views.donor_list, name='donor_list'),

    path('register/', views.register_donor, name='register_donor'),

    path(
        'availability/<int:donor_id>/',
        views.toggle_availability,
        name='toggle_availability'
    ),

]


