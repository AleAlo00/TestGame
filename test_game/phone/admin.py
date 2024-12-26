from django.contrib import admin
from .models import MyPhone

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'get_id_specific') 

    def get_id_specific(self, obj):
        return ", ".join([str(specific.id) for specific in obj.id_specific.all()])
    get_id_specific.short_description = "Specific" 

admin.site.register(MyPhone, PhoneAdmin)