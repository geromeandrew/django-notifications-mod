# Generated by Django 5.2.2 on 2025-06-10 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0009_alter_notification_options_and_more'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='notification',
            new_name='notificatio_recipie_8bedf2_idx',
            old_name='notification_recipient_unread_idx',
        ),
    ]
