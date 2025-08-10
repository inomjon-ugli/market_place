from django.db import models
from django.core.validators import RegexValidator


class Store(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name="Do'kon nomi"
    )
    image = models.ImageField(
        upload_to='store_images/',
        blank=True,
        null=True,
        verbose_name="Do'kon rasmi"
    )
    phone = models.CharField(
        max_length=13,
        blank=True,
        null=True,
        unique=True,
        validators=[RegexValidator(
            r'^\+998\d{9}$',
            'Telefon raqami +998 bilan boshlanishi kerak'
        )],
        verbose_name="Telefon raqami"
    )
    location = models.BigIntegerField(
        verbose_name="Joylashuv ID",
        null=True,
        blank=True
    )
   
    class Meta:
        verbose_name = "Do'kon"
        verbose_name_plural = "Do'konlar"
        ordering = ['name']

    def __str__(self):
        return self.name
