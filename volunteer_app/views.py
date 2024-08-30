# Create your views here.
from django.shortcuts import render, redirect
from .forms import VolunteerForm
from .models import Volunteer

def volunteer_form(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('volunteer_list')
    else:
        form = VolunteerForm()
    return render(request, 'volunteer_form.html', {'form': form})

def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteer_list.html', {'volunteers': volunteers})



def index(request):
    return render(request, 'index.html')
