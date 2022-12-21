from django.urls import path

from . import views

urlpatterns = [
    path('hotels/', views.hoteList, name="hotel-list"),
    path('areas/', views.areaList, name='area-list'),
    path('locations/', views.locationList, name="location-list"),
    path('rooms/<int:pk>/', views.roomDetails, name= "room-details" ),
    path('rooms/', views.roomList, name="room-list"),
    path('hotels/<int:pk>/', views.hotelDetails, name="hotel-details"),
    path('hotels/orders/create/', views.createOrder, name="create-order"),
    path('rooms/available/', views.getAvailableRooms, name="available-rooms"),
]