from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.get_messages),
    path('messages/create/', views.create_message),
    path('messages/<int:id>/', views.get_message),
    path('messages/<int:id>/update/', views.update_message),
    path('messages/<int:id>/delete/', views.delete_message),
]
