from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ('id', 'course_name', 'specialization', 'course_type', 'duration', 'department')
	list_filter = ('course_type', 'department')
	search_fields = ('course_name', 'specialization', 'department__department_name')
