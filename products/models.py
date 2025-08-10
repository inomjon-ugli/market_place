from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(
        max_length=300,
        verbose_name="Mahsulot nomi"
    )
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name="Narx"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Tavsif"
    )
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name="Kategoriya"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Yaratilgan vaqt"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Yangilangan vaqt"
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

    def __str__(self):
        return f"{self.name} - {self.price} so'm"
