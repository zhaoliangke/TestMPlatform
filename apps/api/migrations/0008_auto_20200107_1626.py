# Generated by Django 2.0 on 2020-01-07 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_serviceinfo_status'),
        ('api', '0007_operationinfo_related_case_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GlobalParameter',
            new_name='GlobalParameterInfo',
        ),
        migrations.RenameModel(
            old_name='LocalParameter',
            new_name='LocalParameterInfo',
        ),
    ]