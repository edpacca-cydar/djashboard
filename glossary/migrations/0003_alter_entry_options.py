# Generated by Django 4.1 on 2022-09-06 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0002_domain_acronym'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
    ]
