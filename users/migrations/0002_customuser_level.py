# Generated by Django 3.1.2 on 2020-10-20 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
