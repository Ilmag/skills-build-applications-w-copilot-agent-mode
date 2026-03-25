from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Deleting old data...'))
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        tony = User.objects.create(username='ironman', email='tony@marvel.com')
        steve = User.objects.create(username='captainamerica', email='steve@marvel.com')
        bruce = User.objects.create(username='hulk', email='bruce@marvel.com')
        clark = User.objects.create(username='superman', email='clark@dc.com')
        bruce_dc = User.objects.create(username='batman', email='bruce@dc.com')
        diana = User.objects.create(username='wonderwoman', email='diana@dc.com')

        marvel.members.add(tony, steve, bruce)
        dc.members.add(clark, bruce_dc, diana)

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        pushups = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        running = Workout.objects.create(name='Running', description='Run 5km')

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(user=tony, type='pushups', duration=10, date='2023-01-01')
        Activity.objects.create(user=clark, type='running', duration=30, date='2023-01-02')

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(team=marvel, score=200)
        Leaderboard.objects.create(team=dc, score=180)

        self.stdout.write(self.style.SUCCESS('Ensuring unique index on email...'))
        with connection.cursor() as cursor:
            cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS user_email_unique_idx ON octofit_tracker_user (email);')

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
