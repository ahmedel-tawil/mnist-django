from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('prediction-result/<int:id>', predicted_image, name='prediction-result'),

]
