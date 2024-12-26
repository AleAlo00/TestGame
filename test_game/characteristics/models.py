from django.db import models
from phone.models import MyPhone


# Create your models here.
class MyCharacteristics(models.Model):
    id_cell = models.ForeignKey(MyPhone,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id_cell} - {self.name}"