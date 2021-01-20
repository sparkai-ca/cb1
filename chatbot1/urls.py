
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from chatbot import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('getchatbotresponse/', views.index),
]
