from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        file = options['file']
        print(f"Dzialam: {file}")
