from django.db import models
from phone.models import MyPhone


# Create your models here.
class MyCharacteristics(models.Model):
    id = models.AutoField(primary_key=True)
    id_cell = models.ForeignKey(MyPhone,related_name='id_characteristics',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} - {self.id_cell} - {self.name}"