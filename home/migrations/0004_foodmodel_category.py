# Generated by Django 3.2 on 2023-02-12 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodmodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='home.category'),
        ),
    ]
