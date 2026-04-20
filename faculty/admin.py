from django.contrib import admin
from .models import Faculty


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
	list_display = ('id', 'faculty_name', 'department', 'course', 'experience_years', 'is_hod')
	list_filter = ('department', 'course', 'is_hod')
	search_fields = ('faculty_name', 'qualification', 'department__department_name', 'course__course_name')
