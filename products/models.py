from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    banner = models.ImageField(
        upload_to='product_category_banners/', default='default/category.png')

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(
        upload_to='product_images/', default='default/product.png')

    def __str__(self):
        return self.name
