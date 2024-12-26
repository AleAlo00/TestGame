from django.http import HttpResponse
from django.template import loader

# Create your views here.
def characteristicsPhone(request):
    template = loader.get_template('characteristics.html')
    return HttpResponse(template.render())