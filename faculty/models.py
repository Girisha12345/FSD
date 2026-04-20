from django.db import models
from courses.models import Course
from departments.models import Department


class Faculty(models.Model):
	faculty_name = models.CharField(max_length=150)
	qualification = models.CharField(max_length=150)
	experience_years = models.PositiveIntegerField()
	department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='faculty_members')
	course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='faculty_members')
	is_hod = models.BooleanField(default=False)

	class Meta:
		ordering = ['-is_hod', 'faculty_name']

	def __str__(self):
		role = 'HoD' if self.is_hod else 'Faculty'
		return f'{self.faculty_name} - {role}'
