
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render, redirect,  get_object_or_404
from .models import MyPhone, MyDictCharacteristic, MyFunction


def phones(request):
  myphone = MyPhone.objects.all().values()
  template = loader.get_template('phone.html')
  context = {
    'myphone': myphone,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
    myphone = get_object_or_404(MyPhone, id=id)

    # Recupera le caratteristiche e le funzioni dal database
    characteristics_and_specifics = MyDictCharacteristic.to_dict()

    context = {
        'myphone': myphone,
        'default_characteristics': characteristics_and_specifics,
    }

    return render(request, 'details.html', context)


def detailsF(request, id):
    myphone = get_object_or_404(MyPhone, id=id)

    functions = MyFunction.to_dict()

    context = {
        'myphone': myphone,
        'default_functions': functions,
    }

    return render(request, 'detailsF.html', context)



def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def add_phone(request):
  if request.method == 'POST':
      name = request.POST.get('name')
      date = request.POST.get('date')  

      phone = MyPhone.objects.create(name=name, date=date)

      return redirect('details', id=phone.id) 
  return render(request, 'add_phone.html', {'phone': None}) 


def add_specific(request, phone_id):
    phone = get_object_or_404(MyPhone, id=phone_id)

    if request.method == 'POST':
        characteristic = request.POST.get('characteristic')
        specific = request.POST.get('specific')

        if characteristic and specific:
            # Aggiungi la specifica al telefono
            phone.characteristics[characteristic] = specific
            phone.save()

    return render(request, 'details.html', {'myphone': phone, 'default_characteristics': MyDictCharacteristic.to_dict()})

def add_function(request, phone_id):
    phone = get_object_or_404(MyPhone, id=phone_id)

    if request.method == 'POST':
        function = request.POST.get('function')
        value = request.POST.get('value')
        if function and value:
            phone.functions[function] = value
            phone.save()

    return render(request, 'detailsF.html', {
        'myphone': phone,
        'default_functions': MyFunction.to_dict(),
    })
