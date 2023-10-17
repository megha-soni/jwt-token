# Generated by Django 4.2.6 on 2023-10-16 14:11

import app1.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', app1.manager.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_varified',
            field=models.BooleanField(default=False),
        ),
    ]
