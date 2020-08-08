from pprint import pprint
from django.core.management.base import BaseCommand, CommandError
from pytz import UTC

from app.models import ActivityPeriod, User
from faker import Faker


class Command(BaseCommand):
    help = 'Populate the database with some dummy data'

    def add_arguments(self, parser):
        parser.add_argument('user', nargs=1, type=int)
        parser.add_argument('activity_period', nargs=1, type=int)

    def handle(self, *args, **options):
        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()
        #
        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))

        fake = Faker()
        no_user = options.get('user').pop()
        users = list()
        for _ in range(no_user):
            obj = User.objects.create(real_name=fake.name(), tz=fake.random.randint(0, 593), id=fake.pystr(9, 9))
            users.append(obj.pk)
            pprint(obj)

        no_activity = options.get('activity_period').pop()

        for _ in range(no_activity):
            dt = fake.past_datetime(tzinfo=UTC)

            pprint(ActivityPeriod.objects.create(activity_id=fake.random.choice(users), start_time=dt, end_time=fake.past_datetime(dt, tzinfo=UTC)))

