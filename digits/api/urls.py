from django.urls import path

from .views import DigitViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('digits/', DigitViewSet.as_view(), name= 'digit_list'),
]
