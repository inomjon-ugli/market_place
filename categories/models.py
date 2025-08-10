from django.db import models

class Category(models.Model):
    type_name = models.CharField(
        max_length=250,
        verbose_name="Kategoriya nomi"
    )
    store = models.ForeignKey(
        'stores.Store',
        on_delete=models.CASCADE,
        related_name='categories',
        verbose_name="Do'kon"
    )

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ['type_name']

    def __str__(self):
        return f"{self.name} ({self.store})"
