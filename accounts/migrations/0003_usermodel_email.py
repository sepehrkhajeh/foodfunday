# Generated by Django 3.2 on 2023-01-31 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20230131_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(default=23, max_length=255, unique=True, verbose_name='email address'),
            preserve_default=False,
        ),
    ]
