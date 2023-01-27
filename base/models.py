from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    fullname = models.CharField(max_length=200, null=False, blank=True)
    mothername = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    gen = (("male", "male"), ("female", "female"))
    Gender = models.CharField(max_length=50, choices=gen)
    birthday = models.DateField(null=False, blank=True)
    bloodg = (
        (("A+", "A+")),
        (("A-", "A-")),
        (("B+", "B+")),
        (("B-", "B-")),
        (("AB+", "AB+")),
        (("AB-", "AB-")),
        (("O+", "O+")),
        (("O-", "O-")),
    )
    blood_group = models.CharField(max_length=50, choices=bloodg)
    nationality = models.CharField(max_length=200, null=False, blank=True)
    personalID = models.CharField(max_length=200, null=False, blank=True)
    images = models.ImageField(null=False)
    description = models.TextField(null=True, blank=True)
    docfile = models.FileField(upload_to="documents/%Y/%m/%d")
    license_id = models.CharField(max_length=200, blank=True)
    vehicle_id = models.CharField(max_length=200, null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return str(self.id)


class Account(models.Model):
    account_name = models.CharField(null=True, blank=True)
    account_number = models.PositiveIntegerField(null=True, blank=True)
    account_type = models.CharField(max_length=200, null=False, blank=True)
    amount = models.PositiveIntegerField(null=True, blank=True)
    reg_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return str(self.id)
