# Generated by Django 4.1.6 on 2023-02-19 01:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("agendamento", "0009_schedule_service"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="attendant",
            name="schedule",
        ),
        migrations.AddField(
            model_name="attendant",
            name="schedule",
            field=models.ManyToManyField(
                blank=True, related_name="agendamentos", to="agendamento.schedule"
            ),
        ),
    ]
