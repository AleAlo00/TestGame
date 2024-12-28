from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import MyPhone


def phones(request):
  myphone = MyPhone.objects.all().values()
  template = loader.get_template('phone.html')
  context = {
    'myphone': myphone,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  myphone = MyPhone.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myphone': myphone,
  }
  return HttpResponse(template.render(context, request))

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
