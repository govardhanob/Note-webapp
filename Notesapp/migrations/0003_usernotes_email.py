# Generated by Django 5.0.4 on 2024-04-28 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notesapp', '0002_userdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='usernotes',
            name='email',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Notesapp.userdetails'),
            preserve_default=False,
        ),
    ]
