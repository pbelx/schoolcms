# Generated by Django 3.2.16 on 2022-11-12 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20221112_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='emergencyno',
            field=models.IntegerField(default=911),
        ),
        migrations.AlterField(
            model_name='people',
            name='fathersnumber',
            field=models.IntegerField(default=200000001),
        ),
        migrations.AlterField(
            model_name='people',
            name='mothersnumber',
            field=models.IntegerField(default=10000001),
        ),
    ]