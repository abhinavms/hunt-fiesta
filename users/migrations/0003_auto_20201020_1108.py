# Generated by Django 3.1.2 on 2020-10-20 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
