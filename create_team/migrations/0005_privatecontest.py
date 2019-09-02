# Generated by Django 2.0.2 on 2019-07-31 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0005_users_contests'),
        ('create_team', '0004_auto_20190724_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateContest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_code', models.CharField(max_length=10, unique=True)),
                ('participants', models.TextField()),
                ('contest_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_registration.Users')),
            ],
        ),
    ]
