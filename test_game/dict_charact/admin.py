from django.contrib import admin
from .models import MyDictCharacteristic

# Register your models here.
class MyDictCharacteristicAdmin(admin.ModelAdmin):
    list_display = ("id", "key", "value")

admin.site.register(MyDictCharacteristic, MyDictCharacteristicAdmin)