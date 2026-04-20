from django.contrib import admin
from .models import Bus, TransportRoute


@admin.register(TransportRoute)
class TransportRouteAdmin(admin.ModelAdmin):
	list_display = ('id', 'route_number', 'route_name')
	search_fields = ('route_number', 'route_name')


@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
	list_display = ('id', 'bus_number', 'route', 'total_seats', 'available_seats')
	list_filter = ('route',)
	search_fields = ('bus_number', 'route__route_number', 'route__route_name')
