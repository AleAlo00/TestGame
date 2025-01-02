from django.contrib import admin
from .models import MyPhone, MyDictCharacteristic, MyFunction

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'characteristics', 'functions') 


admin.site.register(MyPhone, PhoneAdmin)

class MyDictCharacteristicAdmin(admin.ModelAdmin):
    list_display = ("id", "key", "value")

admin.site.register(MyDictCharacteristic, MyDictCharacteristicAdmin)

class MyFunctionAdmin(admin.ModelAdmin):
    list_display = ("id", "key", "value")

admin.site.register(MyFunction, MyFunctionAdmin)