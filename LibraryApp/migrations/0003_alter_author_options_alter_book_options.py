# Generated by Django 4.2.6 on 2023-10-27 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name'], 'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title'], 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
    ]