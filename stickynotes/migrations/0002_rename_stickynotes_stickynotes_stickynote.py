# Generated by Django 4.2.3 on 2023-07-31 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stickynotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stickynotes',
            old_name='StickyNotes',
            new_name='StickyNote',
        ),
    ]
