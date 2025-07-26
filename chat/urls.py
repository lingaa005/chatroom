from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view),
    path('messages/', views.get_messages),
    path('send/', views.post_message),
]
