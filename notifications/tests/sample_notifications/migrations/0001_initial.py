# Generated by Django 3.0.5 on 2020-04-11 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('success', 'success'), ('info', 'info'), ('warning', 'warning'), ('error', 'error')], default='info', max_length=20)),
                ('unread', models.BooleanField(db_index=True, default=True)),
                ('actor_object_id', models.CharField(max_length=255)),
                ('verb', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('target_object_id', models.CharField(blank=True, max_length=255, null=True)),
                ('action_object_object_id', models.CharField(blank=True, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('public', models.BooleanField(db_index=True, default=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('emailed', models.BooleanField(db_index=True, default=False)),
                ('data', jsonfield.fields.JSONField(blank=True, null=True)),
                ('details', models.CharField(blank=True, max_length=64, null=True)),
                ('action_object_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_action_object', to='contenttypes.ContentType')),
                ('actor_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notify_actor', to='contenttypes.ContentType')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
                ('target_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_target', to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('-timestamp',),
                'abstract': False,
                'indexes': [
                    models.Index(fields=['recipient', 'unread'], name='notification_recipient_unread_idx'),
                ],
            },
        ),
    ]
