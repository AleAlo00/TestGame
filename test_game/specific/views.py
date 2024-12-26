from django.http import HttpResponse
from django.template import loader

def specifics(request):
  template = loader.get_template('specific.html')
  return HttpResponse(template.render())