# Generated by Django 2.0 on 2020-01-10 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20200110_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operationinfo',
            name='belong_project',
        ),
        migrations.RemoveField(
            model_name='operationinfo',
            name='related_case_id',
        ),
        migrations.AddField(
            model_name='operationinfo',
            name='belong_project_id',
            field=models.CharField(default='', max_length=10, verbose_name='关联项目ID'),
        ),
        migrations.AddField(
            model_name='operationinfo',
            name='related_case',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ApiCaseInfo', verbose_name='关联用例ID'),
        ),
    ]