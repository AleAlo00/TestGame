from django.db import models
from datetime import date

class MyPhone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateField(default=date.today)
    id_specific = models.ManyToManyField("specific.MySpecific")  # Reference to the model via string
    
    def __str__(self):
        specific_ids = ", ".join(map(str, self.id_specific.values_list('id', flat=True)))
        return f"{self.id} - {self.name} - {self.date} - [{specific_ids}]"