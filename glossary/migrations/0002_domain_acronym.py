# Generated by Django 4.1 on 2022-09-06 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='acronym',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]