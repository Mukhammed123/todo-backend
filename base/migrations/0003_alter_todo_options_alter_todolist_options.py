# Generated by Django 4.0.5 on 2022-06-29 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_todo_owner_alter_todo_id_alter_todolist_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['finished']},
        ),
    ]