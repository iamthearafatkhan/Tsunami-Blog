from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.home, name='home'),
    path("about", views.about, name='about'),
    path("history", views.history, name='history'),
    path("real", views.real, name='real'),
    path("safety", views.safety, name='safety'),
    path("discussion", views.discussion, name='discussion'),
    path("faq", views.faq, name='faq'),
    path("add_comment/", views.add_comment, name='add_comment'),  # Endpoint for adding comments

    # APIpaths
    path("faq_chatbot/", views.faq_chatbot, name="faq_chatbot"),
    
    
]


