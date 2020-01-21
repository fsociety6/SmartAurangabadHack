from django.contrib.auth.models import User
from django.db import models
from phone_field import PhoneField


class ExtendedUserModel(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    location = models.IntegerField()
    phone_number = PhoneField(max_length=10)
    user_object = models.OneToOneField(User, related_name='extended_user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_object.username}\'s  Profile'
