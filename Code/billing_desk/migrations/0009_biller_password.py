# Generated by Django 4.0.1 on 2022-04-10 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing_desk', '0008_alter_hospitalbills_fullypaiddate'),
    ]

    operations = [
        migrations.AddField(
            model_name='biller',
            name='password',
            field=models.CharField(default=None, max_length=45),
        ),
    ]
