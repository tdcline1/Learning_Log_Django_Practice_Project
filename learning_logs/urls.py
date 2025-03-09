"""URL patterns for learning_logs APP"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics
    path('topics/', views.topics, name='topics'),
    # Page that shows individual topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page allowing users to add a topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page allowing users to add an entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page allowing users to edit an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]