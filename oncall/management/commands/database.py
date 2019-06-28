from django.core.management.base import BaseCommand, CommandError
from django.core import management
from oncall.models import Oncall
import csv
import os
directory = os.getcwd()

class Command(BaseCommand):
    help = 'Loads LastPass export to Django database'

    # Command functions
    def add_arguments(self, parser):
        parser.add_argument(
            '--file', dest='file', required=False, type=str,
            help='The full path for lastpass csv export',
        )
    def handle(self, *args, **options):
        file = options['file']
        f = open(file)
        csv_f = csv.reader(f)
        for row in csv_f:
            title = row[0]
            start = row[1]
            end = row[2]
            allDay = row[3]
            Oncall.objects.create(title=title, start=start, end=end, allDay=allDay)
