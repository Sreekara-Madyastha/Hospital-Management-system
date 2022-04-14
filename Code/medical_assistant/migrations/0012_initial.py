# Generated by Django 4.0.1 on 2022-04-10 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0003_doctor_age_doctor_salary_doctor_shift'),
        ('receptionist', '0014_initial'),
        ('medical_assistant', '0011_remove_medicalreport_appointment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalAssistant',
            fields=[
                ('MedicalAssistantID', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(default=None, max_length=45)),
                ('FirstName', models.CharField(max_length=45)),
                ('LastName', models.CharField(max_length=45)),
                ('EmailAddress', models.CharField(max_length=45)),
                ('PermantAddress', models.CharField(max_length=100)),
                ('Age', models.IntegerField(default=None)),
                ('Salary', models.IntegerField(default=None)),
                ('Shift', models.IntegerField(default=None)),
                ('BloodGroup', models.CharField(max_length=45)),
                ('contact', models.CharField(default=None, max_length=45)),
                ('underDoctor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalReport',
            fields=[
                ('ReportID', models.IntegerField(primary_key=True, serialize=False)),
                ('report', models.BooleanField(default=False)),
                ('Appointment', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='receptionist.doctorpatientassignment')),
                ('MedicalAssistant', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='medical_assistant.medicalassistant')),
            ],
        ),
    ]
