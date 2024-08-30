from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact_app/contact.html', {'form': form})

def success_view(request):
    return render(request, 'contact_app/success.html')
