import datetime

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


# Create your models here.
class AuthUserManager(BaseUserManager):
    def create_user(self, email, first_name=None, last_name=None, password=None, **extra_fields):
        now = datetime.datetime.now()
        now = timezone.make_aware(now, timezone.get_current_timezone())
        if not first_name:
            raise ValueError('Campo nome obbligatorio')
        if not last_name:
            raise ValueError('Campo cognome obbligatorio')
        user = self.model(email=email, first_name=first_name, last_name=last_name,
                          is_staff=False, is_active=True, is_superuser=False, date_joined=now,
                          last_login=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        u = self.create_user(email, first_name, last_name, password, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u


class AuthUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email', unique=True, db_index=True)
    first_name = models.CharField('Nome', max_length=250)
    last_name = models.CharField('Cognome', max_length=250)
    is_staff = models.BooleanField("Indica se l'utente può accedere all'interfaccia di admin", default=False)
    is_active = models.BooleanField("Attivo", default=False)
    date_joined = models.DateTimeField("Data registrazione", default=timezone.now)
    username = models.CharField('Username', max_length=250, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = AuthUserManager()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Utente'
        verbose_name_plural = 'Utenti'
        ordering = ('first_name', 'last_name', 'email')