# Generated by Django 4.2.16 on 2024-11-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accompany', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accompany',
            name='trip_type',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
