# Generated by Django 3.2.16 on 2022-11-12 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20221112_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='klass',
            field=models.CharField(default='P1', max_length=100),
        ),
    ]