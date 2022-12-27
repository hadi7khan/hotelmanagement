from django.contrib import admin
from .models import Location, Area, Hotel, Room, Order, RoomType

# Register your models here.
admin.site.register(Location)
admin.site.register(Area)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Order)
admin.site.register(RoomType)

