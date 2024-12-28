from django.shortcuts import render
from .forms import MySpecificForm
from characteristics.models import MyCharacteristics

def add_specific(request):
    charact = MyCharacteristics.objects.all()

    if request.method == 'POST':
        form = MySpecificForm(request.POST)
        if form.is_valid():
            form.save()  
    else:
        form = MySpecificForm()

    return render(request, 'add_specific.html', {'form': form, 'characteristics': charact})
