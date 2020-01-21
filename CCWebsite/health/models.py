from django.db import models


# Create your models here.
class Disease(models.Model):
    ID1 = models.IntegerField()
    name = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'
