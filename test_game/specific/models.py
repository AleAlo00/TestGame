from django.db import models
from characteristics.models import MyCharacteristics

# Create your models here.
class MySpecific(models.Model):
    id = models.AutoField(primary_key=True)
    id_charact = models.ForeignKey(MyCharacteristics,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} - {self.id_charact} - {self.name}"