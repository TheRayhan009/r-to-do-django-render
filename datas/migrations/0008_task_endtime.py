<<<<<<< HEAD
# Generated by Django 5.0.7 on 2024-09-18 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datas', '0007_task_enddate_alter_task_user_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='EndTime',
            field=models.CharField(max_length=55, null=True),
        ),
    ]
=======
# Generated by Django 5.0.7 on 2024-09-18 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datas', '0007_task_enddate_alter_task_user_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='EndTime',
            field=models.CharField(max_length=55, null=True),
        ),
    ]
>>>>>>> origin/main
