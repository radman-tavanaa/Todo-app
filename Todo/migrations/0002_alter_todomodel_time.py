# Generated by Django 3.2.12 on 2022-04-07 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]
