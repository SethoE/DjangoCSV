# Generated by Django 4.0.2 on 2022-04-28 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileConverter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='CSV')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('fileID', models.AutoField(primary_key=True, serialize=False)),
                ('uploadDate', models.DateField()),
                ('filename', models.CharField(max_length=100)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
        ),
    ]
