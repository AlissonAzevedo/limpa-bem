# Generated by Django 4.1.6 on 2023-02-18 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("agendamento", "0006_schedule_service_value_alter_client_state_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="schedule",
            name="attendant",
        ),
        migrations.AlterField(
            model_name="employee",
            name="position",
            field=models.CharField(
                choices=[("gerente", "Gerente"), ("helper", "Helper")],
                max_length=100,
                verbose_name="Cargo:",
            ),
        ),
        migrations.CreateModel(
            name="Attendant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default=None, max_length=255)),
                (
                    "schedule",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="agendamentos",
                        to="agendamento.schedule",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="usuario",
                    ),
                ),
            ],
            options={
                "verbose_name": "Atendente",
                "verbose_name_plural": "Atendentes",
            },
        ),
    ]
