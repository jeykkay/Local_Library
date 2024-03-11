# Generated by Django 4.2.11 on 2024-03-06 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookcopy',
            options={'verbose_name': 'Book Copy', 'verbose_name_plural': 'Book Copies'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Country', 'verbose_name_plural': 'Countries'},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Authors',
            new_name='author',
        ),
    ]