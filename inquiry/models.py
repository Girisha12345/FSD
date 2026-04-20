from django.db import models
from courses.models import Course


class Inquiry(models.Model):
	student_name = models.CharField(max_length=150)
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='inquiries')
	consent = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f'{self.student_name} - {self.course.course_name}'
