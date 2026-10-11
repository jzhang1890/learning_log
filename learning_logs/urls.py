"""Defines URL patterns for learning_logs"""

from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('about/', views.about,name = 'about'),
    path('topics/', views.topics, name = 'topics'),
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),
    # Page for adding new topics
    path('new_topic/', views.new_topic, name = 'new_topic'),
    # Page for adding new entries
    path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),
    # Page for editing a topic.
    path('edit_topic/<int:topic_id>/', views.edit_topic, name = 'edit_topic'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry'),
    # Page for deleting a topic.
    path('topics/<int:topic_id>/delete/', views.topic_delete, name='topic_delete'),
]