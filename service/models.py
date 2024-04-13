from django.db import models


class Service_category(models.Model):
    name = models.CharField(max_length=100)
    banner = models.ImageField(
        upload_to='service_banners/', default='default/default_banner.jpg')
    description = models.TextField()

    def __str__(self):
        return self.name
