from rest_framework import serializers

from .models import Hostel


class HostelSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.course_name', read_only=True)
    course_specialization = serializers.CharField(source='course.specialization', read_only=True)

    class Meta:
        model = Hostel
        fields = [
            'id',
            'hostel_name',
            'room_type',
            'total_rooms',
            'available_rooms',
            'course',
            'course_name',
            'course_specialization',
        ]
