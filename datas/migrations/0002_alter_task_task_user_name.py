# Generated by Django 5.0.7 on 2024-08-19 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_user_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
