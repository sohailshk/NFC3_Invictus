from django.shortcuts import render, redirect
from .models import Resource
from .forms import BulkResourceForm
from .forms import ResourceForm


def update_all_resources(request):
    resources = Resource.objects.all()
    if request.method == 'POST':
        form = BulkResourceForm(request.POST, resources=resources)
        if form.is_valid():
            for resource in resources:
                name = form.cleaned_data.get(f'name_{resource.pk}')
                quantity = form.cleaned_data.get(f'quantity_{resource.pk}')
                
                if name and quantity is not None:
                    resource.name = name
                    resource.quantity = quantity
                    resource.save()

            return redirect('resource_update_success')
    else:
        form = BulkResourceForm(resources=resources)

    return render(request, 'resources/resource_list.html', {'resources': resources, 'form': form})


def update_success(request):
    # This view will display a confirmation message or updated resource list
    return render(request, 'resources/update_success.html')


def createresource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resource_update_all')  # Redirect back to resource list after saving
    else:
        form = ResourceForm()
    
    return render(request, 'resources/resource_create.html', {'form': form})
