from django.db import models

# Create your models here.
class TodoModel(models.Model):
    name=models.CharField(max_length=45)
    email = models.EmailField(max_length=50)
    work = models.CharField(max_length=200)
    time = models.TimeField()