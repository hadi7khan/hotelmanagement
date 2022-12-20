from django.db import models

class Location(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self) -> str:
    return self.name


class Area(models.Model):
  name = models.CharField(max_length=200)
  location = models.ForeignKey(Location, related_name="location_area", on_delete=models.CASCADE, default=1)

  def __str__(self):
    return self.name

class Hotel(models.Model):
  name = models.CharField(max_length=200)
  area = models.ForeignKey(Area, related_name="hotel_area", on_delete=models.CASCADE)
  hoteltype = models.CharField(max_length=100)


  def __str__(self):
    return self.name

class RoomType(models.Model):
  type = models.CharField(max_length=100)

  def __str__(self):
    return self.type

class Room(models.Model):
  room_no = models.IntegerField()
  hotel = models.ForeignKey(Hotel, related_name= "hotel_room", on_delete=models.CASCADE)
  room_type = models.ForeignKey(RoomType, related_name="room_type", on_delete=models.SET_NULL, null=True)
  attached_bathroom = models.BooleanField(default=False)
  bed = models.CharField(max_length=10)
  entertainment = models.BooleanField(default=False)


  def __str__(self):
    return str(self.room_no)

