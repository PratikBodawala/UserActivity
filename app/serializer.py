from pytz import all_timezones
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from app.models import User, ActivityPeriod


class ActivityPeriodSerializer(ModelSerializer):
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()

    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time',)


class UserSerializer(ModelSerializer):
    tz = serializers.CharField(source='get_tz_display')

    class Meta:
        model = User
        depth = 1
        fields = ('id', 'real_name', 'tz',)
