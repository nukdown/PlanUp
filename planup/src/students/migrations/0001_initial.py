# Generated by Django 2.0.4 on 2018-05-08 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_student', models.CharField(max_length=40)),
                ('email_student', models.EmailField(max_length=40)),
                ('password_student', models.CharField(max_length=14)),
                ('registration_student', models.CharField(max_length=14)),
                ('age_of_birth_student', models.CharField(max_length=14)),
                ('gender_student', models.CharField(max_length=14)),
            ],
        ),
    ]
