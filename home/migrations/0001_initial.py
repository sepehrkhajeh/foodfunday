# Generated by Django 3.2 on 2023-01-31 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_food', models.CharField(max_length=250, verbose_name='نام غذا')),
                ('price', models.PositiveIntegerField(verbose_name='قیمت')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='درباره غذا')),
                ('img', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name': ' غذا ها',
            },
        ),
    ]
