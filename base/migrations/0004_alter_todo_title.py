# Generated by Django 4.0.5 on 2022-07-01 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_todo_options_alter_todolist_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
