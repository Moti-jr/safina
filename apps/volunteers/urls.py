from django.urls import path
from . import views

app_name = 'volunteers'

urlpatterns = [
    path('', views.VolunteerView.as_view(), name='volunteer'),
]
