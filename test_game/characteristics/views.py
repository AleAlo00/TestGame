from django.shortcuts import render
from .forms import MyCharacteristicsForm
from phone.models import MyPhone  

def add_characteristics(request, phone_id):
    phone = MyPhone.objects.get(id=phone_id)  
    if request.method == 'POST':
        form = MyCharacteristicsForm(request.POST)  
        if form.is_valid():  
            characteristic = form.save(commit=False)  
            characteristic.phone = phone  
            characteristic.save()  
    else:
        form = MyCharacteristicsForm()  

    return render(request, 'add_characteristics.html', {'form': form, 'phone': phone})
