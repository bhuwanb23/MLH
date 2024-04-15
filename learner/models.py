# Import the models module from django.db
from django.db import models

# Define the Document model
class Document(models.Model):
    # Define the id field as an AutoField with primary_key set to True
    id = models.AutoField(primary_key=True)

    # Define the title field as a CharField with a maximum length of 255 characters
    title = models.CharField(max_length=255)

    # Define the subject field as a CharField with a maximum length of 25 characters
    subject = models.CharField(max_length=25)

    # Define the pdf field as a FileField with the upload_to argument set to 'learner\materials-pdf'
    pdf = models.FileField(upload_to='learner\materials-pdf')