# Generated by Django 3.1.1 on 2020-10-05 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='lose',
            new_name='play',
        ),
    ]
