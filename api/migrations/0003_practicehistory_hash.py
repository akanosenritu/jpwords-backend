# Generated by Django 3.1.3 on 2020-12-11 12:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201206_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='practicehistory',
            name='hash',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]