# Generated by Django 4.1.6 on 2023-02-18 22:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("agendamento", "0005_remove_schedule_employee_schedule_attendant_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="schedule",
            name="service_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=7,
                null=True,
                verbose_name="Valor do Serviço:",
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="state",
            field=models.CharField(max_length=100, verbose_name="Estado:"),
        ),
        migrations.AlterField(
            model_name="services",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=7, verbose_name="Preço:"
            ),
        ),
    ]
