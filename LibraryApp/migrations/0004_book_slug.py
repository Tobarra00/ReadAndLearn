# Generated by Django 4.2.6 on 2023-10-29 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0003_alter_author_options_alter_book_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(unique=True, null=True),
        ),
    ]