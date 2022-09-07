from django.urls import path
from hackathon.views import index, team


urlpatterns = [
    path('', index, name='hackathon-home'),
    path('team/', team, name='hackathon-team'),
]
