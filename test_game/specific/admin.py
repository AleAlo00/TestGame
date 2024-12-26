from django.contrib import admin
from .models import MySpecific

# Register your models here.
class SpecificAdmin(admin.ModelAdmin):
    list_display = ("id","id_charact","name")

admin.site.register(MySpecific,SpecificAdmin)