# Generated by Django 4.1.1 on 2022-09-24 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0002_cashbook_created_at_cashbook_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashbook',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='cashbook',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
