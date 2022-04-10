from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vacation
from .forms import VacationForm
from django.views.generic import ListView, DetailView
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from rest_framework import viewsets
from .serializers import VacationSerializer


 
def home(request):
    return render(request,"vacation_aiia/index.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
class IndexView(ListView):
    template_name = 'vacation_aiia/index.html'
    context_object_name = 'vacation_list'

    def get_queryset(self):
        return Vacation.objects.all()
    
class VacationViewSet(viewsets.ModelViewSet):
    queryset = Vacation.objects.all().order_by('title')
    serializer_class = VacationSerializer
    
class ContactDetailView(DetailView):
    model = Vacation
    template_name = 'vacation_aiia/vacation-detail.html'
    
def create(request):
    if request.method == 'POST':
        form = VacationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = VacationForm()
    form.fields['from_date'].widget = DateTimePickerInput();
    form.fields['to_date'].widget = DateTimePickerInput();

    return render(request,'vacation_aiia/create.html',{'form': form})

def edit(request, pk, template_name='vacation_aiia/edit.html'):
    vacation = get_object_or_404(Vacation, pk=pk)
    form = VacationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})


def delete(request, pk, template_name='vacation_aiia/confirm_delete.html'):
    vacation = get_object_or_404(Vacation, pk=pk)
    if request.method=='POST':
        vacation.delete()
        return redirect('index')
    return render(request, template_name, {'object':vacation})