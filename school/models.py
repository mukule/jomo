from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    logo = models.ImageField(upload_to='school_logos/',
                             default='default/logo.png')
    banner = models.ImageField(
        upload_to='banner/', default='default/school_banner.png')

    def __str__(self):
        return self.tag


class Course(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    flyer = models.ImageField(
        upload_to='course_flyers/', default='default/flyer.png')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)  # Adding price field

    def __str__(self):
        return self.name
