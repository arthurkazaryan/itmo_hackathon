from django.urls import path
from accounts.views import RegisterUser, LoginUser, logout_user, ProfilePage, LocationPage


urlpatterns = [
    path('projects/', ProfilePage.as_view(), name='accounts-locations'),
    path('projects/<int:id>', LocationPage.as_view(), name='accounts-locations-location'),
    # path('settings/', SettingsPage.as_view(), name='accounts-settings'),
    path('register/', RegisterUser.as_view(), name='accounts-register'),
    path('login/', LoginUser.as_view(), name='accounts-login'),
    path('logout/', logout_user, name='accounts-logout')
]
