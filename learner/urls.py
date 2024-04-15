# Import the admin module from django.contrib
from django.contrib import admin

# Import the path function from django.urls
from django.urls import path

# Import the view functions from learner.views
from learner.views import home, material, quiz, open_pdf

# Define the URL patterns for the learner app
urlpatterns = [
    # Define the home URL pattern that maps to the home view function
    path('', home, name='home'),

    # Define the material URL pattern that maps to the material view function
    path('material/', material, name='material'),

    # Define the quiz URL pattern that maps to the quiz view function
    path('quiz/', quiz, name='quiz'),

    # Define the open_pdf URL pattern that maps to the open_pdf view function
    path('open-pdf/<int:document_id>/', open_pdf, name='open_pdf'),
]