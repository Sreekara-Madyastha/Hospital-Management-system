# Generated by Django 4.0.1 on 2022-04-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_assistant', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalassistant',
            name='password',
            field=models.CharField(default=None, max_length=45),
        ),
    ]
