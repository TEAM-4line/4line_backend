# Generated by Django 5.1.1 on 2024-11-15 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0005_alter_test_trip_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='trip_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
