from django.contrib import admin

# Register your models here.
from app.models import User, ActivityPeriod

#
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'real_name', 'tz')
#
#
# class ActivityPeriodAdmin(admin.ModelAdmin):
#     list_display = ('active_id', 'start_time', 'end_time')


admin.site.register(ActivityPeriod)
admin.site.register(User)
