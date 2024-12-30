
from django.db import models

# Dizionario predefinito
DEFAULT_CHARACTERISTICS = {
    "RAM": ["2GB", "4GB", "8GB", "16GB", "32GB"],
    "Color": ["Black", "White", "Red", "Blue", "Green"],
    "Storage": ["16GB", "32GB", "64GB", "128GB", "256GB"],
    "OS": ["Android", "iOS"],
    "Camera": ["5MP", "8MP", "12MP", "16MP", "20MP"],
}

class MyDictCharacteristic(models.Model):
    # ID univoco
    id = models.AutoField(primary_key=True)
    # Chiave del dizionario
    key = models.CharField(max_length=100, unique=True)
    # Valori associati, memorizzati come stringa separata da virgole
    value = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.key}"

    @classmethod
    def populate_from_dict(cls, dictionary):
        """
        Popola il modello con i dati di un dizionario predefinito.
        """
        for key, values in dictionary.items():
            # Converte la lista in una stringa separata da virgole
            value_str = ",".join(values)
            # Crea o aggiorna il record
            obj, created = cls.objects.get_or_create(key=key, defaults={"value": value_str})
            if not created and obj.value != value_str:
                obj.value = value_str  # Aggiorna solo se il valore è diverso
                obj.save()

    @classmethod
    def to_dict(cls):
        """
        Ritorna un dizionario con i dati del modello.
        """
        data = {}
        for obj in cls.objects.all():
            # Converte la stringa separata da virgole in una lista
            data[obj.key] = obj.value.split(",")
        return data
