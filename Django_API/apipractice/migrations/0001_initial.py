# Generated by Django 3.1.2 on 2021-05-20 07:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('account', models.TextField()),
                ('phone', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField()),
            ],
        ),
    ]
