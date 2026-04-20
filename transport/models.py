from django.db import models


class TransportRoute(models.Model):
	route_number = models.CharField(max_length=20)
	route_name = models.CharField(max_length=150)

	class Meta:
		ordering = ['route_number']

	def __str__(self):
		return f'Route {self.route_number} - {self.route_name}'


class Bus(models.Model):
	bus_number = models.CharField(max_length=30)
	total_seats = models.PositiveIntegerField()
	available_seats = models.PositiveIntegerField()
	route = models.ForeignKey(TransportRoute, on_delete=models.CASCADE, related_name='buses')

	class Meta:
		ordering = ['bus_number']

	def __str__(self):
		return f'Bus {self.bus_number} ({self.route.route_number})'
