from django.db import models
from departments.models import Department


class Course(models.Model):
	COURSE_TYPE_CHOICES = [
		('UG', 'UG'),
		('PG', 'PG'),
	]

	course_name = models.CharField(max_length=200)
	specialization = models.CharField(max_length=200)
	course_type = models.CharField(max_length=2, choices=COURSE_TYPE_CHOICES)
	duration = models.CharField(max_length=50)
	department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')

	class Meta:
		ordering = ['course_name']

	def __str__(self):
		return f'{self.course_name} ({self.specialization})'
