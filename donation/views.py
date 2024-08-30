from django.shortcuts import render, redirect
from .forms import DonationForm
from .models import Donation

def create_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('donation_list')
    else:
        form = DonationForm()
    return render(request, 'donation/create_form.html', {'form': form})

def donation_list(request):
    donations = Donation.objects.all()
    return render(request, 'donation/donation_list.html', {'donations': donations})


def donate_view(request):
    return render(request, 'donation/donate_page.html')
