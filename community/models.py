from django.db import models

# Create your models here.
class Community(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    trip_start = models.DateField()
    trip_end = models.DateField()
    region = models.CharField(max_length=50)
    rating = models.FloatField()
    content = models.TextField(max_length=500)
    photo = models.ImageField()