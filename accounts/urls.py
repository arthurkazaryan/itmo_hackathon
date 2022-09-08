from django.urls import path
from accounts.views import RegisterUser, LoginUser, logout_user, ProfilePage, LocationPage


urlpatterns = [
    path('locations/', ProfilePage.as_view(), name='accounts-locations'),
    path('locations/<int:id>', LocationPage.as_view(), name='accounts-locations-location'),
    path('register/', RegisterUser.as_view(), name='accounts-register'),
    path('login/', LoginUser.as_view(), name='accounts-login'),
    path('logout/', logout_user, name='accounts-logout')
]
