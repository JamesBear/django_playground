# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
import datetime

def index(request):
    template = loader.get_template('home/index.html')
    context = RequestContext(request, {
        'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        })
    return HttpResponse(template.render(context))