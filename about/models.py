from django.db import models

# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=100)
    year_started = models.IntegerField()
    tag = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
