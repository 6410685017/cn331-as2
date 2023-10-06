# Generated by Django 4.2.6 on 2023-10-06 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('s_id', models.IntegerField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('sub_id', models.CharField(max_length=5, primary_key='True', serialize=False)),
                ('sub_name', models.CharField(max_length=64)),
                ('capacity', models.IntegerField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]