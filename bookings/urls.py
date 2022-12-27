from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:pk>/', views.createBooking, name="create-booking")
]
