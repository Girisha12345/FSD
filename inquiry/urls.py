from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('courses/', views.courses_page, name='courses-page'),
    path('faculty/', views.faculty_page, name='faculty-page'),
    path('hostel/', views.hostel_page, name='hostel-page'),
    path('transport/', views.transport_page, name='transport-page'),
    path('api/register/', views.InquiryRegisterAPIView.as_view(), name='api-register'),
    path('api/courses/', views.CourseListAPIView.as_view(), name='api-courses'),
    path('api/faculty/<int:course_id>/', views.FacultyByCourseAPIView.as_view(), name='api-faculty-by-course'),
    path('api/hostel/', views.HostelListAPIView.as_view(), name='api-hostel'),
    path('api/transport/', views.TransportListAPIView.as_view(), name='api-transport'),
]
