from django.contrib import admin
from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
	list_display = ('id', 'student_name', 'email', 'phone', 'course', 'consent', 'created_at')
	list_filter = ('consent', 'course', 'created_at')
	search_fields = ('student_name', 'email', 'phone', 'course__course_name', 'course__specialization')
	ordering = ('-created_at',)
