from django.urls import path
from .views import CurrentTimeView


urlpatterns = [
    path('current-time', CurrentTimeView.as_view(), name='current-time')
]