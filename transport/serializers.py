from rest_framework import serializers

from .models import Bus, TransportRoute


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['id', 'bus_number', 'total_seats', 'available_seats']


class TransportRouteSerializer(serializers.ModelSerializer):
    buses = BusSerializer(many=True, read_only=True)
    buses_available = serializers.SerializerMethodField()

    class Meta:
        model = TransportRoute
        fields = ['id', 'route_number', 'route_name', 'buses_available', 'buses']

    def get_buses_available(self, obj):
        return obj.buses.count()
