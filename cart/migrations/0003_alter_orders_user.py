# Generated by Django 3.2 on 2023-02-10 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0002_rename_product_orderitems_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL, verbose_name='مشتری'),
        ),
    ]
