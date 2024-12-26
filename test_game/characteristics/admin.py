from django.contrib import admin
from .models import MyCharacteristics

# Register your models here.
class CharacteristicsAdmin(admin.ModelAdmin):
    list_display = ("id_cell","name")

admin.site.register(MyCharacteristics,CharacteristicsAdmin)