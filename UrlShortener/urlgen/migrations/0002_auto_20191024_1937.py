# Generated by Django 2.2.4 on 2019-10-24 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlgen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.URLField(unique=True),
        ),
    ]