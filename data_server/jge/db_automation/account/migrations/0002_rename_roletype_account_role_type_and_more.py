# Generated by Django 5.1.3 on 2025-02-06 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='roleType',
            new_name='role_type',
        ),
        migrations.RenameField(
            model_name='accountroletype',
            old_name='roleType',
            new_name='role_type',
        ),
    ]
