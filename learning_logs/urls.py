# Defines URL patterns for learning_logs.

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all topics
    path('topics/', views.topics, name='topics'),

    # Page with detailed info about topic
    path('topics/<topic_id>/', views.topic, name='topic')
]
