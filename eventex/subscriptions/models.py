from django.db import models
import uuid


class Subscription(models.Model):
    name: models.CharField = models.CharField('nome', max_length=100)
    cpf: models.CharField = models.CharField('CPF', max_length=11)
    email: models.EmailField = models.EmailField('e-mail')
    phone: models.CharField = models.CharField('telefone', max_length=20)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    uid: models.UUIDField = models.UUIDField(default=uuid.uuid4, editable=False)
    paid: models.BooleanField = models.BooleanField('pago', default=False)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
