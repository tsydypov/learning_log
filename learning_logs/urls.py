# Defines URL patterns for learning_logs.

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all topics
    path('topics/', views.topics, name='topics'),

    # Page with detailed info about topic
    path('topics/<topic_id>/', views.topic, name='topic'),

    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),

    path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),
]
