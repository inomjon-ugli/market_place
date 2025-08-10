from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator




class Users(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(
            max_length=13,
            blank=True,
            null=True,
            unique=True,
            validators=[RegexValidator(r'^\+998\d{9}$', 'Telefon raqami +998 bilan boshlanishi kerak')]
        )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = "users"
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
        ordering = ['id']

    