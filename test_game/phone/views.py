
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect,  get_object_or_404
from .models import MyPhone
from dict_charact.models import DEFAULT_CHARACTERISTICS


def phones(request):
  myphone = MyPhone.objects.all().values()
  template = loader.get_template('phone.html')
  context = {
    'myphone': myphone,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
    myphone = get_object_or_404(MyPhone, id=id)

    # Prepara la lista di specifiche per ogni caratteristica
    characteristics_and_specifics = DEFAULT_CHARACTERISTICS

    context = {
        'myphone': myphone,
        'default_characteristics': characteristics_and_specifics,
    }

    return render(request, 'details.html', context)

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
  if request.method == "POST":
      specific = request.POST.get('specific')
      myphone = get_object_or_404(MyPhone, id=phone_id)
      # Aggiungi la specifica al telefono (modifica come necessario)
      myphone.specifics.append(specific)
      myphone.save()
      return redirect('phone_detail', phone_id=phone_id)
