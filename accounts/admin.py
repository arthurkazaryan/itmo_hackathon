from django.contrib import admin
from django.contrib.admin import display
from accounts.models import Profile, UserLocation


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'date_joined', 'chat_id')
    readonly_fields = ('user', 'first_name', 'date_joined', 'chat_id')

    @display()
    def first_name(self, obj):
        return obj.user.first_name

    @display()
    def date_joined(self, obj):
        return obj.user.date_joined

    search_fields = ('user__username',)


@admin.register(UserLocation)
class UserLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'location_uuid', 'title', 'address', 'status', 'date')
    # readonly_fields = ('user', 'location_uuid', 'date')
    search_fields = ('user__username',)
