from django.urls import path
from . import views

app_name = 'donations'

urlpatterns = [
    path('', views.DonateView.as_view(), name='donate'),
]
