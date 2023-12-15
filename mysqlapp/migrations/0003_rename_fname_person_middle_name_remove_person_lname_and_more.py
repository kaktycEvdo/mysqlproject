# Generated by Django 5.0 on 2023-12-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysqlapp', '0002_rename_код_клиента_client_clientid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='fname',
            new_name='middle_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='person',
            name='mname',
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
