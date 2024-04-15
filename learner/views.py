# Import the render function from django.shortcuts
from django.shortcuts import render
#importing the models
from .models import Document

# Define the home view function
def home(request):
    # Render the index.html template with an empty context dictionary
    return render(request, 'index.html')

# Define the material view function
def material(request):
    # Render the material.html template with an empty context dictionary
    return render(request,'material.html')

# Define the quiz view function
def quiz(request):
    # Render the quiz.html template with an empty context dictionary
    return render(request,'quiz.html')

#define a open pdf function

def open_pdf(request, document_id):
    return render(request, 'open_pdf.html', {'document': document})