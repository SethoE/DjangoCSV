# Generated by Django 4.0.2 on 2022-04-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('is_authenticated', models.BooleanField(default=False)),
            ],
        ),
    ]
