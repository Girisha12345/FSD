from rest_framework import serializers

from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.department_name', read_only=True)

    class Meta:
        model = Course
        fields = [
            'id',
            'course_name',
            'specialization',
            'course_type',
            'duration',
            'department',
            'department_name',
        ]
