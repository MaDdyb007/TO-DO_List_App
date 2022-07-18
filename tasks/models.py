from django.db import models
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    