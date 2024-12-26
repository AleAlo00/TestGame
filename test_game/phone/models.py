from django.db import models
from datetime import date

# Create your models here.
class MyPhone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateField(default=date.today())
    
    def __str__(self):
        return f"{self.id} - {self.name} - {self.date}"

