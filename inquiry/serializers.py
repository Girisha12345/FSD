from rest_framework import serializers

from .models import Inquiry


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ['id', 'student_name', 'email', 'phone', 'course', 'consent', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_phone(self, value):
        normalized = ''.join(ch for ch in value if ch.isdigit())
        if len(normalized) < 10:
            raise serializers.ValidationError('Enter a valid phone number with at least 10 digits.')
        return value

    def validate_consent(self, value):
        if not value:
            raise serializers.ValidationError('Consent is required to register an inquiry.')
        return value
