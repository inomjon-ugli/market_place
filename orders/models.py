from django.db import models
from django.conf import settings


class PaymentType(models.TextChoices):
    CASH = 'cash', 'Naqd pul'
    CARD = 'card', 'Karta orqali'
    CLICK = 'click', "Click to'lov tizimi"
    PAYME = 'payme', "Payme to'lov tizimi"


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name='orders'
    )
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )
    amount = models.PositiveIntegerField()
    date_of_order = models.DateTimeField(auto_now_add=True)
    payment_type = models.CharField(
        max_length=20,
        choices=PaymentType.choices
    )

    class Meta:
        db_table = 'orders'
        ordering = ['-date_of_order']
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'

    @property
    def total_price(self):
        return self.price * self.amount
