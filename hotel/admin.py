from django.contrib import admin
from .models import Location, Area, Hotel, Room

# Register your models here.
admin.site.register(Location)
admin.site.register(Area)
admin.site.register(Hotel)
admin.site.register(Room)
