# Generated by Django 5.0.4 on 2024-04-15 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_alter_service_category_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.ImageField(default='default/service_icon.png', upload_to='service_icons/'),
        ),
    ]
