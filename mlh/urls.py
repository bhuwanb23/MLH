# Import the admin module from django.contrib
from django.contrib import admin

# Import the path and include functions from django.urls
from django.urls import path, include

# Define the URL patterns for the project
urlpatterns = [
    # Define the admin URL pattern that maps to the admin site
    path('admin/', admin.site.urls),

    # Define the URL pattern that includes the URL patterns for the learner app
    path('', include('learner.urls')),
]