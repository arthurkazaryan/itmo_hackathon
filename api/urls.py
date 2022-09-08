from django.urls import path
from api import views

urlpatterns = [
    path('v1/get/customers', views.get_customers),
    path('v1/post/customers', views.post_customers)
]
