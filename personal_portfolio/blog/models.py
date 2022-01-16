from django.db import models

# Create your models here.
class Project(models.Model):
    """
    Creating an instance a class and inheriting from a model class.
    """
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="templates/images/")
    #Blank is a property that can be added to anything.
    url = models.URLField(blank=True)