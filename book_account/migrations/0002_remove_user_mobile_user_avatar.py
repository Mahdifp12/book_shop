# Generated by Django 4.1.3 on 2023-02-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='تصویر آواتار'),
        ),
    ]
