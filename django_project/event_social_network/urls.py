from django.urls import path
from event_social_network import views

urlpatterns =[
    path('', views.home, name='home'),
    path('about/', views.about, name= 'about'),
    path('create/', views.create_event, name='create_event'),
    path('search/', views.user_search, name='user_search'),
    path('events/', views.all_events, name='all_events'),
    path('event/<int:event_id>/delete/', views.delete_event, name='delete_event'),
    path('event/<int:event_id>/edit/', views.edit_event, name='edit_event'),

]