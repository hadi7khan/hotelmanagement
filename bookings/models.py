from django.db import models
from django.contrib.auth.models import User
from hotel.models import Room


class Bookings(models.Model):
    user = models.ForeignKey(
        User, related_name="user_booking", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        Room, related_name="booked_hotel_detail", on_delete=models.CASCADE
    )
    days = models.IntegerField()
    added_meals = models.BooleanField(default=False)
    meals_price = models.IntegerField()
    check_in = models.DateField()
    check_out = models.DateField()
