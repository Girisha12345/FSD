from django.contrib import admin
from .models import Hostel


@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
	list_display = ('id', 'hostel_name', 'room_type', 'total_rooms', 'available_rooms', 'course')
	list_filter = ('room_type', 'course')
	search_fields = ('hostel_name', 'course__course_name', 'course__specialization')
