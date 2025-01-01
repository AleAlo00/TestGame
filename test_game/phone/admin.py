from django.contrib import admin
from .models import MyPhone, MyDictCharacteristic

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'characteristics') 


admin.site.register(MyPhone, PhoneAdmin)

class MyDictCharacteristicAdmin(admin.ModelAdmin):
    list_display = ("id", "key", "value")

admin.site.register(MyDictCharacteristic, MyDictCharacteristicAdmin)