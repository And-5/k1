from django.db import models


class Client(models.Model):
    STATUS_CHOICES = [
        ('lead', 'Лид'),
        ('client', 'Клиент'),
    ]
    fio = models.CharField('ФИО', max_length=255)
    balance = models.DecimalField('Баланс', max_digits=12, decimal_places=2, default=0)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='active')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.fio
