from django.db import models


class Service_category(models.Model):
    name = models.CharField(max_length=100)
    banner = models.ImageField(
        upload_to='service_banners/', default='default/default_banner.jpg')
    header = models.ImageField(
        upload_to='service_headers/', default='default/header.png')
    description = models.TextField()

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(Service_category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='service_icons/',
                             default='default/service_icon.png')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
