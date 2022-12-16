from rest_framework import serializers

from .models import Hotel, Area, Location, Room

class HotelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hotel
    fields = "__all__"

class AreaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Area
    fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
  hotel = serializers.SerializerMethodField(read_only=True)
  class Meta:
    model = Room
    fields = "__all__"

  def get_hotel(self, obj):
    hotel = obj.hotel.name
    return hotel

class RoomdetailsSerializer(serializers.ModelSerializer):
  hotel = serializers.SerializerMethodField(read_only=True)
  class Meta:
    model = Room
    fields = ["id", "room_no", "hotel"]

  def get_hotel(self, obj):
    hotel = obj.hotel.name
    return hotel