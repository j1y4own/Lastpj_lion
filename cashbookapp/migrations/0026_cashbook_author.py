# Generated by Django 4.0.6 on 2022-10-30 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cashbookapp', '0025_alter_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashbook',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
