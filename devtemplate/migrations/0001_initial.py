# Generated by Django 3.2.13 on 2022-07-19 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DevTemplate',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('dcf1d3fa-a31a-424d-8f46-ce0260f7ce27'), editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=80)),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('img', models.ImageField(blank=True, default='upload/none.jpg', upload_to='image')),
                ('device_type', models.CharField(blank=True, max_length=40)),
                ('is_custom_registered', models.BooleanField(default=False)),
                ('protocol_type', models.CharField(choices=[('MQTT', 'MQTT'), ('HTTP', 'HTTP'), ('CoAP', 'CoAP')], default='HTTP', max_length=200)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
