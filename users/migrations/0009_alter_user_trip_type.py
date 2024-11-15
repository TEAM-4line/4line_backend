# Generated by Django 5.1.1 on 2024-11-15 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_is_staff_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='trip_type',
            field=models.CharField(blank=True, choices=[('lion', '사자'), ('owl', '부엉이'), ('monkey', '원숭이'), ('dolphin', '돌고래'), ('fox', '여우'), ('cat', '고양이')], default='lion', max_length=20, null=True),
        ),
    ]
