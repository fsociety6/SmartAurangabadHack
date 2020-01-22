from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Disease(models.Model):
    ID1 = models.IntegerField()
    name = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'

class Crowdsource(models.Model):
    choice=[('MALE','Male'),('FEMALE','Female')]
    disease=[('TYPHOID','typhoid'),('DELIRIA','deliria'),('DENGUE','dengue'),('MALARIA','malaria')]
    Age=models.IntegerField()
    Gender=models.CharField(max_length=10, choices=choice)
    Created_By=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    Disease=models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,blank=True)

#gramseva
    def __str__(self):
        return f'{self.created_date}'