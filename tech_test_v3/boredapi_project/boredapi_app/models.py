from django.db import models

# Create your models here.
class Activity(models.Model):
    activity = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    participants = models.PositiveIntegerField()
    price = models.FloatField()
    key = models.CharField(max_length=255)

    def __str__(self):
        return self.activity