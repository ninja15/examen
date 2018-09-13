# Generated by Django 2.1.1 on 2018-09-13 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=150)),
                ('last_name', models.CharField(db_index=True, max_length=150)),
                ('number_of_login', models.IntegerField()),
            ],
        ),
    ]
