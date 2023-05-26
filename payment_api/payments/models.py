from django.db import models
from django.contrib.auth.models import User
import uuid


class Payment(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('DEBIT', 'Debit'),
        ('CREDIT', 'Credit'),
    ]

    SEDE = [
        ('Barranquilla', 'Barranquilla'),
        ('Cartagena', 'Cartagena'),
        ('Santa Marta', 'Santa Marta'),
        ('Sincelejo', 'Sincelejo'),
        ('Monteria', 'Monteria'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    card_number = models.CharField(max_length=16, null=True)
    cvv = models.IntegerField(null=True)
    expiration_date = models.DateField(null=True)
    sede = models.CharField(max_length=20, choices=SEDE, default='Barranquilla')
    description = models.CharField(max_length=200, null=True)
    datetime = models.DateTimeField(auto_now=True)
    cuotas = models.IntegerField(null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    error = models.BooleanField()
    bank=models.CharField(max_length=30)