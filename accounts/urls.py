from django.urls import path
from accounts.views import RegisterUser, LoginUser, logout_user#, ProfilePage, SettingsPage, UserProjectPage


urlpatterns = [
    path('projects/', LoginUser.as_view(), name='accounts-projects'),
    # path('projects/project/<int:id>', UserProjectPage.as_view(), name='accounts-projects-project'),
    # path('settings/', SettingsPage.as_view(), name='accounts-settings'),
    path('register/', RegisterUser.as_view(), name='accounts-register'),
    path('login/', LoginUser.as_view(), name='accounts-login'),
    path('logout/', logout_user, name='accounts-logout')
]
