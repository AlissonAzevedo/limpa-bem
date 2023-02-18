# django
from django.db import models
from django.contrib.auth.models import User

# app
from agendamento.choices import COMPANY_POSITION, STATUS_SCHEDULE, METHOD_PAYMENT


class BaseModel(models.Model):
    created_at = models.DateTimeField("Criação:", auto_now_add=True)
    updated_at = models.DateTimeField("Atualização:", auto_now=True)


class Services(BaseModel):
    name = models.CharField("Serviço:", max_length=100)
    price = models.DecimalField("Preço:", max_digits=5, decimal_places=2)
    active = models.BooleanField("Ativo:", default=True)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(
        User, verbose_name="Usuário", on_delete=models.CASCADE, default=None
    )
    name = models.CharField(max_length=255, default=None)
    position = models.CharField("Cargo:", max_length=100, choices=COMPANY_POSITION)

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    def __str__(self):
        return self.name

    def is_manager(self):
        return self.position == "gerente"

    def get_position(self):
        return [
            i[1]
            for i in Employee._meta.get_field("position").choices
            if i[0] == self.position
        ][0]

    def set_name_default(self):
        if self.name is None:
            self.name = self.user.username


class Client(models.Model):
    name = models.CharField("Nome:", max_length=100)
    street = models.CharField("Rua:", max_length=60)
    number = models.CharField("Número:", max_length=10)
    district = models.CharField("Bairro:", max_length=60)
    city = models.CharField("Cidade:", max_length=60)
    state = models.CharField("Estado:", max_length=2)
    zipcode = models.CharField("CEP:", max_length=9)
    phone = models.CharField("Telefone:", max_length=20)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.name

    @property
    def address(self):
        return (
            self.street
            + ", "
            + self.number
            + " - "
            + self.district
            + " - "
            + self.city
            + " - "
            + self.state
            + " - "
            + self.zipcode
        )


class Schedule(BaseModel):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    attendant = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="atendente",
        default=None
    )
    helper = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="ajudante",
        default=None
    )
    payment = models.CharField(
        "Metodo de Pagamento:", max_length=100, choices=METHOD_PAYMENT
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField("Data do atendimento:")
    status = models.CharField("Situação:", max_length=100, choices=STATUS_SCHEDULE)

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"

    def __str__(self):
        return self.client.name

    def get_service_value(self):
        return str(self.service.price)
