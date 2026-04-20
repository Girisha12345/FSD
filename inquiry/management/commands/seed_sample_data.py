from django.core.management.base import BaseCommand

from courses.models import Course
from departments.models import Department
from faculty.models import Faculty
from hostel.models import Hostel
from transport.models import Bus, TransportRoute


class Command(BaseCommand):
    help = 'Load sample data for Chanakya University Inquiry System.'

    def handle(self, *args, **options):
        cse_dept, _ = Department.objects.get_or_create(department_name='Computer Science')
        ece_dept, _ = Department.objects.get_or_create(department_name='Electronics and Communication')
        mgmt_dept, _ = Department.objects.get_or_create(department_name='Management Studies')

        btech_cse, _ = Course.objects.get_or_create(
            course_name='BTech',
            specialization='Computer Science',
            defaults={'course_type': 'UG', 'duration': '4 Years', 'department': cse_dept},
        )
        btech_ec, _ = Course.objects.get_or_create(
            course_name='BTech',
            specialization='Electronics and Communication',
            defaults={'course_type': 'UG', 'duration': '4 Years', 'department': ece_dept},
        )
        mba, _ = Course.objects.get_or_create(
            course_name='MBA',
            specialization='Finance and Marketing',
            defaults={'course_type': 'PG', 'duration': '2 Years', 'department': mgmt_dept},
        )

        Faculty.objects.get_or_create(
            faculty_name='Dr. Kavita Rao',
            qualification='PhD in Computer Science',
            experience_years=14,
            department=cse_dept,
            course=btech_cse,
            is_hod=True,
        )
        Faculty.objects.get_or_create(
            faculty_name='Prof. Suresh Nair',
            qualification='MTech',
            experience_years=9,
            department=ece_dept,
            course=btech_ec,
            is_hod=True,
        )
        Faculty.objects.get_or_create(
            faculty_name='Dr. Ananya Iyer',
            qualification='PhD in Management',
            experience_years=12,
            department=mgmt_dept,
            course=mba,
            is_hod=True,
        )

        Hostel.objects.get_or_create(
            hostel_name='Chanakya Residency A',
            room_type='Single',
            total_rooms=120,
            available_rooms=34,
            course=btech_cse,
        )
        Hostel.objects.get_or_create(
            hostel_name='Chanakya Residency B',
            room_type='Double',
            total_rooms=160,
            available_rooms=52,
            course=btech_ec,
        )
        Hostel.objects.get_or_create(
            hostel_name='Chanakya Residency C',
            room_type='Shared',
            total_rooms=180,
            available_rooms=68,
            course=mba,
        )

        route_1, _ = TransportRoute.objects.get_or_create(route_number='R1', route_name='City Center Loop')
        route_2, _ = TransportRoute.objects.get_or_create(route_number='R2', route_name='North Corridor Line')

        Bus.objects.get_or_create(
            bus_number='KA-01-1001',
            total_seats=50,
            available_seats=17,
            route=route_1,
        )
        Bus.objects.get_or_create(
            bus_number='KA-01-1002',
            total_seats=50,
            available_seats=9,
            route=route_1,
        )
        Bus.objects.get_or_create(
            bus_number='KA-01-2001',
            total_seats=45,
            available_seats=14,
            route=route_2,
        )

        self.stdout.write(self.style.SUCCESS('Sample university data loaded successfully.'))
