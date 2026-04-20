from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics, status
from rest_framework.response import Response

from courses.models import Course
from courses.serializers import CourseSerializer
from faculty.models import Faculty
from faculty.serializers import FacultySerializer
from hostel.models import Hostel
from hostel.serializers import HostelSerializer
from transport.models import TransportRoute
from transport.serializers import TransportRouteSerializer

from .models import Inquiry
from .serializers import InquirySerializer


@ensure_csrf_cookie
def home_page(request):
	return render(request, 'home.html')


def courses_page(request):
	courses = Course.objects.select_related('department').all()
	return render(request, 'courses.html', {'courses': courses})


def faculty_page(request):
	selected_course_id = request.GET.get('course_id')
	faculty_qs = Faculty.objects.select_related('department', 'course').all()

	if selected_course_id:
		faculty_qs = faculty_qs.filter(course_id=selected_course_id)

	context = {
		'courses': Course.objects.all(),
		'faculty_members': faculty_qs,
		'selected_course_id': int(selected_course_id) if selected_course_id and selected_course_id.isdigit() else None,
	}
	return render(request, 'faculty.html', context)


def hostel_page(request):
	hostels = Hostel.objects.select_related('course').all()
	return render(request, 'hostel.html', {'hostels': hostels})


def transport_page(request):
	routes = TransportRoute.objects.prefetch_related('buses').all()
	return render(request, 'transport.html', {'routes': routes})


class InquiryRegisterAPIView(generics.CreateAPIView):
	queryset = Inquiry.objects.all()
	serializer_class = InquirySerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return Response(
			{
				'message': 'Inquiry registered successfully.',
				'data': serializer.data,
			},
			status=status.HTTP_201_CREATED,
		)


class CourseListAPIView(generics.ListAPIView):
	queryset = Course.objects.select_related('department').all()
	serializer_class = CourseSerializer


class FacultyByCourseAPIView(generics.ListAPIView):
	serializer_class = FacultySerializer

	def get_queryset(self):
		return Faculty.objects.select_related('department', 'course').filter(course_id=self.kwargs['course_id'])


class HostelListAPIView(generics.ListAPIView):
	queryset = Hostel.objects.select_related('course').all()
	serializer_class = HostelSerializer


class TransportListAPIView(generics.ListAPIView):
	queryset = TransportRoute.objects.prefetch_related('buses').all()
	serializer_class = TransportRouteSerializer
