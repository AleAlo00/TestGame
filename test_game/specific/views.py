from django.shortcuts import render
from .forms import MySpecificForm
from characteristics.models import MyCharacteristics, MyPhone

def add_specific(request, phone_id):
    phone = MyPhone.objects.get(id=phone_id)
    
    charact = MyCharacteristics.objects.filter(id_cell=phone,id_specific__isnull=True)
    
    if request.method == 'POST':
        form = MySpecificForm(request.POST)
        if form.is_valid():
            specific = form.save()

            phone.id_specific.add(specific)
    else:
        form = MySpecificForm()

    return render(request, 'add_specific.html', {'form': form, 'characteristic': charact, 'phone': phone})
