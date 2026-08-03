from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('',        views.GalleryView.as_view(), name='gallery'),
    path('videos/', views.VideoView.as_view(),   name='videos'),
]
