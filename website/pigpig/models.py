from django.db import models

# Create your models here.
class part(models.Model):
    name = models.CharField(max_length=10, unique=True)
    english = models.CharField(max_length=20)
    taste = models.TextField()
    cooking = models.TextField()
    recipename = models.CharField(max_length=20)
    recipename2 = models.CharField(max_length=20)
    recipe = models.TextField()
    pic1 = models.CharField(max_length=50)
    pic2 = models.CharField(max_length=50)
    pic3 = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name
