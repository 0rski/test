# Generated by Django 2.1.1 on 2018-10-03 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20181003_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='un',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='User_details',
        ),
    ]