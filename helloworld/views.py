from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contact
from django.urls import reverse_lazy

# Create your views here.
# def hello(request):
    # return HttpResponse('Hello World!')

class ContactList(ListView): 
    model = Contact

class ContactDetail(DetailView): 
    model = Contact

class ContactCreate(CreateView): 
    model = Contact
    fields = '__all__'
    success_url = reverse_lazy('contact_list')

   
class ContactUpdate(UpdateView): 
    model = Contact
    fields = '__all__'
    success_url = reverse_lazy('contact_list')

class ContactDelete(DeleteView): 
    model = Contact
    fields = '__all__'
    success_url = reverse_lazy('contact_list')