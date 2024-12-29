from django.contrib import admin
from .models import MyPhone

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date') 


admin.site.register(MyPhone, PhoneAdmin)