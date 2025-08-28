from django.urls import path
from .views import word_cloud_view

urlpatterns = [
    path('wordcloud/', word_cloud_view, name='word_cloud'),
]