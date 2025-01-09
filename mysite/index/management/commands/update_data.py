from django.core.management.base import BaseCommand
from index.utils import update_parsed_data


class Command(BaseCommand):
    help = 'Update parsed data'

    def handle(self, *args, **kwargs):
        update_parsed_data()
        self.stdout.write('Data updated successfully.')
