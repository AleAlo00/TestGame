from django.shortcuts import render
from .forms import MyCharacteristicsForm
from phone.models import MyPhone  

def add_characteristics(request):
    phones = MyPhone.objects.all()  
    if request.method == 'POST':
        form = MyCharacteristicsForm(request.POST)
        if form.is_valid():
            form.save() 
    else:
        form = MyCharacteristicsForm()

    return render(request, 'add_characteristics.html', {'form': form, 'phones': phones})
