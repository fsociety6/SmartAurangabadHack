# Generated by Django 2.2.5 on 2020-01-22 04:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0005_auto_20200121_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='crowdsource',
            name='location',
            field=models.CharField(default=django.utils.timezone.now, max_length=6),
            preserve_default=False,
        ),
    ]