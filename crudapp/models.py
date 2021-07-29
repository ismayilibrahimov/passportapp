from django.core.validators import FileExtensionValidator
from django.db import models
from softdelete.models import SoftDeleteObject


class Customer(SoftDeleteObject, models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=256)


class Passport(SoftDeleteObject, models.Model):
    objects = models.Manager()
    scan_file = models.FileField(
        upload_to='passports/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'png'])], null=True, blank=True)
    document_number = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    patronymic = models.CharField(max_length=256)
    nationality = models.CharField(max_length=256)
    birth_date = models.DateField()
    personal_number = models.CharField(max_length=256)
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    issue_date = models.DateField()
    expire_date = models.DateField()
    issuing_authority = models.CharField(max_length=256)
    customer = models.ForeignKey(
        Customer, related_name='passports', on_delete=models.CASCADE, null=True, blank=True)
