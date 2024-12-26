from django.db import models
from datetime import date

class MyPhone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateField(default=date.today)
    id_specific = models.ManyToManyField("specific.MySpecific")  # Riferimento al modello tramite stringa
    
    def __str__(self):
        specific_ids = ", ".join(str(specific.id) for specific in self.id_specific.all())
        return f"{self.id} - {self.name} - {self.date} - [{specific_ids}]"