from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from .models import Bookings
from hotel.models import Room


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def createBooking(request, pk):
  data = request.data
  user = request.user
  room = Room.objects.filter(check_in__range=(data['check_in'], data['check_out'])).filter(check_out__range=(data['check_in'], data['check_out'])).filter(booked=False).filter(hotel__id=pk)[0]
  print(room.id)
  # r = room.get
  print(room)
  booking = Bookings.objects.create(
    room = room,
    user = user,
    days = data['days'],
    added_meals = data['added_meals'],
    meals_price = data['meals_price'],
    check_in = data['check_in'],
    check_out = data['check_in'],
)
  room.booked = True
  room.save()

  return Response("booked successfully")
