import pandas as pd
from django.core.management import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        file = options['file']
        df = pd.read_csv(file)
        referrer_email = []
        for index, row in df.iterrows():
            if not pd.isna(row['referrer_email']):
                referrer_email.append(row['referrer_email'])
            user = User.objects.create(username=row['email'], first_name=row['first_name'], last_name=row['last_name'],
                                       email=row['email'])
            user.profile.points = row['balance']
            user.profile.save()
            user.save()
        for referrer in referrer_email:
            try:
                user = User.objects.get(email=referrer)
                user.profile.points += 20
                user.profile.save()
            except User.DoesNotExist:
                print(f'User with {referrer} does not exist')
