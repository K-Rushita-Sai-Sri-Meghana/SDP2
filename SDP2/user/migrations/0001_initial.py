# Generated by Django 3.2.3 on 2021-05-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=30)),
                ('phoneno', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'user_table',
            },
        ),
    ]
