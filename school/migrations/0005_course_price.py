# Generated by Django 5.0.4 on 2024-04-15 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_course_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
