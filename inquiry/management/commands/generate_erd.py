from pathlib import Path

from django.conf import settings
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = 'Generate ER diagram image from Django models.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--output',
            default='er_diagram.png',
            help='Output file path relative to project root (default: er_diagram.png).',
        )

    def handle(self, *args, **options):
        output_path = Path(settings.BASE_DIR) / options['output']

        # Use django-extensions graph_models to export the ER diagram image.
        call_command(
            'graph_models',
            'departments',
            'courses',
            'faculty',
            'hostel',
            'transport',
            'inquiry',
            group_models=True,
            all_applications=False,
            output=str(output_path),
        )

        self.stdout.write(self.style.SUCCESS(f'ER diagram generated: {output_path}'))
