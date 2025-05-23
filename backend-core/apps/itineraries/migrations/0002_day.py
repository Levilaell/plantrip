# Generated by Django 5.2 on 2025-05-01 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('itinerary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='itineraries.itinerary')),
            ],
        ),
    ]
