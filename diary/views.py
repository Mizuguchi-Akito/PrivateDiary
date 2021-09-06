from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
# Create your views here.
def index(request):
    return render(request, 'diary/index.html')

class IndexView(generic.TemplateView):
    template_name="diary/index.html"