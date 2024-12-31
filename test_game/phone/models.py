from django.db import models
from datetime import date

class MyPhone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateField(default=date.today)
    characteristics = models.JSONField(default=dict) 
    image_url = models.URLField(default="https://via.placeholder.com/250")
    

    def __str__(self):
        return f"{self.id} - {self.name} - {self.date} - {self.characteristics}"