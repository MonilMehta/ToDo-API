# Generated by Django 4.2 on 2024-01-29 13:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("TodoAPI", "0002_todo_username"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todo",
            old_name="username",
            new_name="user",
        ),
    ]