# Generated by Django 2.1.2 on 2018-10-01 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

from base.models import FriendlyNameMixin
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('loser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_lost', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_won', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
            bases=(models.Model, FriendlyNameMixin),
        ),
    ]
