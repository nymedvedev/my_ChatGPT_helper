# Generated by Django 5.0.2 on 2024-03-06 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StandaloneTraffic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('username', models.CharField(max_length=255)),
                ('request', models.TextField()),
                ('response', models.TextField()),
            ],
        ),
    ]