from rest_framework import serializers

from .models import Faculty


class FacultySerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.department_name', read_only=True)
    course_name = serializers.CharField(source='course.course_name', read_only=True)

    class Meta:
        model = Faculty
        fields = [
            'id',
            'faculty_name',
            'qualification',
            'experience_years',
            'department',
            'department_name',
            'course',
            'course_name',
            'is_hod',
        ]
