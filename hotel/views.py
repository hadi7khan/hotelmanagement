from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Hotel, Area, Location, Room
from .serializers import HotelSerializer, AreaSerializer, LocationSerializer, RoomdetailsSerializer, RoomSerializer

@api_view(["GET"])
def hoteList(request):
  hotels = Hotel.objects.all()
  serializer = HotelSerializer(hotels, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def areaList(request):
  areas = Area.objects.all()
  serializer = AreaSerializer(areas, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def locationList(request):
  locations = Location.objects.all()
  serializer = LocationSerializer(locations, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def roomList(request):
  rooms = Room.objects.all()
  serializer = RoomSerializer(rooms, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def roomDetails(request, pk):
  roomDetails = Room.objects.get(pk=pk)
  serializer = RoomdetailsSerializer(roomDetails, many=False)
  return Response(serializer.data)
