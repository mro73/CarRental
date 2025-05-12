from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Address(models.Model):
    user = models.ForeignKey(User, related_name='user_address_set', on_delete=models.RESTRICT)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    post_code = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    building_no = models.CharField(max_length=50)
    appartment_no = models.CharField(max_length=50, blank=True)

class User(User):
    IDENTITY_DOCUMENT_TYPES = [
        ("dowod_osobisty", "Dowód osobisty"),
        ("prawo_jazdy", "Prawo jazdy"),
        ("paszport", "Paszport"),
        ("legitymacja_studencka", "Legitymacja studencka")
    ]
    phone = PhoneNumberField()
    birth_date = models.DateField()
    identity_document_type = models.CharField(max_length=50, choices=IDENTITY_DOCUMENT_TYPES)
    identity_document_no = models.CharField(max_length=50)
    address = models.OneToOneField(Address, related_name= 'user_address_set', on_delete=models.CASCADE)