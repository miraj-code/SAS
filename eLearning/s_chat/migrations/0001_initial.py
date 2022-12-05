# Generated by Django 4.0.4 on 2022-06-08 03:46

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('a_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
                ('description', models.TextField()),
                ('profile_picture', models.ImageField(upload_to='Chat Group Profile Pictures')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Chat Group',
                'verbose_name_plural': 'Chat Groups',
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='ChatGroupMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_chat.chatgroup')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_user.student')),
            ],
            options={
                'verbose_name': 'Chat Group Message',
                'verbose_name_plural': 'Chat Group Messages',
            },
        ),
    ]