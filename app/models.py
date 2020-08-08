from datetime import datetime
from pytz import all_timezones
from django.contrib.auth.models import User as AuthUser
from django.db import models


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=9)  # assuming max_length from test.json file
    tz = models.IntegerField(choices=enumerate(all_timezones))
    real_name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.id}: {self.real_name}'


class ActivityPeriod(models.Model):
    activity = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.activity} from {self.start_time} to {self.end_time}'
