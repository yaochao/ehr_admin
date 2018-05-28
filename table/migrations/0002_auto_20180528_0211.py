# Generated by Django 2.0.5 on 2018-05-28 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('auto_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tab_name', models.CharField(max_length=64)),
                ('col_name', models.CharField(max_length=64)),
                ('col_comment', models.CharField(max_length=1024)),
                ('col_ver', models.IntegerField()),
                ('data_type', models.CharField(max_length=64)),
                ('is_nullable', models.SmallIntegerField(default=1)),
                ('col_status', models.SmallIntegerField(default=1)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'ehr_columns',
                'ordering': ['auto_id'],
            },
        ),
        migrations.RemoveField(
            model_name='table',
            name='id',
        ),
        migrations.AlterField(
            model_name='table',
            name='tab_name',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='table',
            table='ehr_tables',
        ),
    ]