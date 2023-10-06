# Generated by Django 4.2.6 on 2023-10-06 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0002_alter_student_s_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectStudentList',
            fields=[
                ('subject', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='regist.subject')),
                ('students', models.ManyToManyField(to='regist.student')),
            ],
        ),
    ]