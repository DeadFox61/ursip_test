from django.core.management import BaseCommand

from data_analysis.services import create_data_from_exel_file


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_data_from_exel_file()
