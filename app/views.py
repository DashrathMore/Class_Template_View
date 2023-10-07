from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.views.generic import TemplateView
from app.forms import *

class temp(TemplateView):
    template_name = 'temp.html'

class form(TemplateView):
    template_name= 'form.html'
    def get_context_data(self, **kwargs):
        edo=super().get_context_data(**kwargs)
        edo['name']='Dashrath'
        edo['surname']='More'
        edo['so']=StudForm
        return edo
    def post(self,request):
        sfdo=StudForm(request.POST)
        if sfdo.is_valid():
            sfdo.save()
            return HttpResponse('Data Inserted.....')