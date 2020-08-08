from django.urls import path
from app.views import ActivityPeriodApi, UserApi, UserActivityView

urlpatterns = [
    path('user/', UserApi.as_view()),
    path('activityperiod/', ActivityPeriodApi.as_view()),
    path('user-activity/', UserActivityView.as_view())
]
