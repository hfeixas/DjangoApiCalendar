# Generated by Django 2.1.5 on 2019-01-21 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oncall', '0002_auto_20190121_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oncall',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]