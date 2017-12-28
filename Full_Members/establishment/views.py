from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from establishment.models import establishment
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request, 'establishment/index.html')


class addEstablishment(CreateView):
    model = establishment
    fields = '__all__'


class editEstablishment(UpdateView):
    model = establishment
    fields = '__all__'


class viewEstablishment(DetailView):
    model = establishment
    context_object_name = 'single_establishment'
    template_name = 'establishment/details.html'


class listEstablishment(ListView):
    model = establishment
    context_object_name = 'all_establishments'




class delEstablishment(DeleteView):
    model = establishment
    success_url = reverse_lazy('establishment:List')
