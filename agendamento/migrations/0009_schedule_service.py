# Generated by Django 4.1.6 on 2023-02-18 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("agendamento", "0008_remove_schedule_service"),
    ]

    operations = [
        migrations.AddField(
            model_name="schedule",
            name="service",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="agendamento.services",
            ),
        ),
    ]
