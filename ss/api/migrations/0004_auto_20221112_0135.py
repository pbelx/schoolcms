# Generated by Django 3.2.16 on 2022-11-12 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20221112_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='klass',
            field=models.CharField(default='test', max_length=100),
        ),
        migrations.AddField(
            model_name='people',
            name='name',
            field=models.CharField(default='test', max_length=100),
        ),
        migrations.AddField(
            model_name='people',
            name='password',
            field=models.CharField(default='test', max_length=100),
        ),
    ]