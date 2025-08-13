from django.db import models
from django.conf import settings

class Cards_of_users(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cards',
        verbose_name='Foydalanuvchi',

    )
    card_number = models.CharField(
        max_length=16,
        verbose_name='Karta raqami',
        help_text = '16 xonali raqamni kiriting'
    )
    expire_date = models.DateField(verbose_name='Amal qilish muddati')