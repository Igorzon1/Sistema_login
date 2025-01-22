from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, cpf, password=None, **extra_fields):
        if not cpf:
            raise ValueError("O CPF é obrigatório")
        user = self.model(cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("O superusuário deve ter is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("O superusuário deve ter is_superuser=True.")

        return self.create_user(cpf, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    CPF_LENGTH = 11
    cpf = models.CharField(max_length=CPF_LENGTH, unique=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True, default="email@exemplo.com")
    cargo_choices = [
        ('Administrador', 'Administrador'),
        ('Gerente', 'Gerente'),
        ('Funcionario', 'Funcionário'),
    ]
    cargo = models.CharField(max_length=15, choices=cargo_choices, default='Funcionario')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Adiciona um nome único
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Adiciona um nome único
        blank=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.cpf
