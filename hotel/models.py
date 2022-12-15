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

  def __str__(self):
    return self.name

class Room(models.Model):
  room_no = models.IntegerField()
  hotel = models.ForeignKey(Hotel, related_name= "hotel_room", on_delete=models.CASCADE)

  def __str__(self):
    return self.room_no