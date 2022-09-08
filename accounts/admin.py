from django.contrib import admin
from django.contrib.admin import display
from accounts.models import Profile, UserLocation, LocationCamera, CustomerDataRegistration


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


@admin.register(LocationCamera)
class LocationCameraAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'camera_uuid', 'video', 'title', 'status', 'date')
    # readonly_fields = ('user', 'location', 'camera_uuid', 'video', 'date')
    search_fields = ('user__username',)


@admin.register(CustomerDataRegistration)
class CustomerDataRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'camera', 'count', 'warning_flag', 'date')
    # readonly_fields = ('user', 'camera', 'count', 'warning', 'time')
    search_fields = ('user__username',)
