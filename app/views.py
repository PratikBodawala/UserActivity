from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import User, ActivityPeriod
from app.serializer import UserSerializer, ActivityPeriodSerializer
from rest_framework import generics


class UserApi(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityPeriodApi(generics.ListAPIView):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer


class UserActivityView(APIView):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        user = UserSerializer(users, many=True)
        for _ in user.data:
            _['activity_periods'] = ActivityPeriodSerializer(ActivityPeriod.objects.filter(activity__id=_.get('id')),
                                                             many=True).data

        return Response({
            'ok': True,
            'members': user.data,
        })
