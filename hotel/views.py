from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status

from .models import Hotel, Area, Location, Room, Order
from .serializers import (
    HotelSerializer,
    AreaSerializer,
    LocationSerializer,
    RoomdetailsSerializer,
    RoomSerializer,
    HotelDetailSerializer,
    CreateOrder
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["name"] = user.name
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def hoteList(request):
    hotels = Hotel.objects.all()
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def areaList(request):
    areas = Area.objects.all()
    serializer = AreaSerializer(areas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def locationList(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def roomList(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    response = {
        "status": "Success",
        "code": status.HTTP_200_OK,
        "message": "Room List fetched Successfully",
        "data": serializer.data,
    }
    return Response(response, status=status.HTTP_200_OK)


@api_view(["GET"])
def roomDetails(request, pk):
    try:
        roomDetails = Room.objects.get(pk=pk)
        serializer = RoomdetailsSerializer(roomDetails, many=False)
        response = {
            "status": "Success",
            "code": status.HTTP_200_OK,
            "message": "Room details fetched succesfully",
            "data": serializer.data,
        }
        return Response(response)
    except:
        response = {
            "status": "FAilure",
            "code": status.HTTP_404_NOT_FOUND,
            "message": "Room does not exist",
            "data": [],
        }
        return Response(response)


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def hotelDetails(request, pk):
    # try:
    hotel = Hotel.objects.get(pk=pk)

    serializer = HotelDetailSerializer(hotel, many=False)
    response = {
        "status": "Success",
        "code": status.HTTP_200_OK,
        "message": "Hotel details fetched succesfully",
        "data": serializer.data,
    }
    return Response(response)

    # except:
    #   response = {
    #     "status": "FAilure",
    #     "code": status.HTTP_404_NOT_FOUND,
    #     "message": "Hotel does not exist",
    #     "data": []
    #   }
    #   return Response(response)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def createOrder(request):
    # print(request.data)
    data = request.data
    user = request.user
    room = Room.objects.get(pk=data["room"])
    order = Order.objects.create(
        room=room,
        user=user,
        price=data["price"],
        days=data["days"],
        added_meals=data["added_meals"],
        meals_price=data["meals_price"],
    )
    room.booked = True
    room.save()
    # order.save()
    
    return Response("Room booked successfully!", status=status.HTTP_201_CREATED)

@api_view(['GET'])
def getAvailableRooms(request):
    rooms = Room.objects.filter(booked=False)
    serializer = RoomSerializer(rooms, many=True)

    response = {
        "status": "Success",
        "code": status.HTTP_200_OK,
        "message": "Available Rooms fetched succesfully",
        "data": serializer.data,
    }
    return Response(response)