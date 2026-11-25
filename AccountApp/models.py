from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


number_validator = RegexValidator(regex=r'^\d{8}$', message='Phone number must be 8 digits')


def validate_birth_date(value):
    if value >= timezone.localdate():
        raise ValidationError('Birth date cannot be in the future.')


class User(AbstractUser):
    pass


class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True)
    phone = models.CharField(max_length=8, validators=[number_validator])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Doctors'
        verbose_name = 'Doctor'


class Patient(User):
    national_id = models.CharField(max_length=8, unique=True, validators=[number_validator])
    phone = models.CharField(max_length=8, validators=[number_validator])
    birth_date = models.DateField(validators=[validate_birth_date])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Patients'
        verbose_name = 'Patient'


class Speciality(models.Model):
    name = models.CharField(max_length=255)
    doctors = models.ManyToManyField(Doctor, related_name='specialities')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Specialities'
        verbose_name = 'Speciality'
    def __str__(self):
        return self.name