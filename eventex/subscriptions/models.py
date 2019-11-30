from django.db import models


class Subscription(models.Model):
    name: models.CharField = models.CharField(max_length=100)
    cpf: models.CharField = models.CharField(max_length=11)
    email: models.EmailField = models.EmailField()
    phone: models.CharField = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
