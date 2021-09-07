from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from.forms import InquiryForm
# Create your views here.
def index(request):
    return render(request, 'diary/index.html')

class IndexView(generic.TemplateView):
    template_name="diary/index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm