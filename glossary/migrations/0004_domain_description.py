# Generated by Django 4.1 on 2022-09-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0003_alter_entry_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='description',
            field=models.CharField(default='', max_length=2000),
            preserve_default=False,
        ),
    ]