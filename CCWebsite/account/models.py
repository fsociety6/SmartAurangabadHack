from django.contrib.auth.models import User
from django.db import models
from phone_field import PhoneField


class ExtendedUserModel(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    location = models.DecimalField(max_digits=6, decimal_places=0)
    phone_number = models.DecimalField(max_digits=10, decimal_places=0)
    user_object = models.OneToOneField(User, related_name='extendeduser', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_object.username}\'s  Profile'
