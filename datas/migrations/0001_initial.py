<<<<<<< HEAD
# Generated by Django 5.0.7 on 2024-08-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_user_name', models.CharField(max_length=255)),
                ('user_task', models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=100)),
                ('Lname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
=======
# Generated by Django 5.0.7 on 2024-08-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_user_name', models.CharField(max_length=255)),
                ('user_task', models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=100)),
                ('Lname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
>>>>>>> origin/main
