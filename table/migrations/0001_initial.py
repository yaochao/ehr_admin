# Generated by Django 2.0.5 on 2018-05-24 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tab_name', models.CharField(max_length=64)),
                ('tab_comment', models.CharField(max_length=1024)),
                ('tab_ver', models.IntegerField()),
                ('tab_buzz', models.SmallIntegerField()),
                ('tab_type', models.SmallIntegerField(default=1)),
                ('tab_status', models.SmallIntegerField(default=1)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['tab_name'],
            },
        ),
    ]
