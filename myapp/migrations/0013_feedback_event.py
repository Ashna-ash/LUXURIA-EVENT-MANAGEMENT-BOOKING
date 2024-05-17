# Generated by Django 5.0.4 on 2024-05-09 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_remove_feedback_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.event'),
            preserve_default=False,
        ),
    ]
