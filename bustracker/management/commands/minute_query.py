from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = '<Doesnt Take Any Arguments>'
    help = 'Makes a query on all stations along a bus line and adds them to the database'

    def handle(self, *args, **options):
        self.stdout.write('Hello World')