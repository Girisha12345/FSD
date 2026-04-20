from django.db import models
from courses.models import Course


class Hostel(models.Model):
	ROOM_TYPE_CHOICES = [
		('Single', 'Single'),
		('Double', 'Double'),
		('Shared', 'Shared'),
	]

	hostel_name = models.CharField(max_length=150)
	room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES)
	total_rooms = models.PositiveIntegerField()
	available_rooms = models.PositiveIntegerField()
	course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='hostel_facilities')

	class Meta:
		ordering = ['hostel_name']

	def __str__(self):
		return f'{self.hostel_name} - {self.room_type}'
