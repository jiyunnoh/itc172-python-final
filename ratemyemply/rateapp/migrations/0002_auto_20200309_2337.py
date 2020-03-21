# Generated by Django 2.2.9 on 2020-03-09 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rateapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='reviewuser',
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='company',
            name='companylocation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]