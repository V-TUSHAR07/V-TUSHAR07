# Generated by Django 4.2.6 on 2023-11-01 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a01', '0002_blog_alter_contact_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='content',
            new_name='desc',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
    ]
