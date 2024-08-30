from django import forms
from .models import Resource


class BulkResourceForm(forms.Form):

    def __init__(self, *args, **kwargs):
        resources = kwargs.pop('resources', [])
        super().__init__(*args, **kwargs)
        for resource in resources:
            self.fields[f'name_{resource.pk}'] = forms.CharField(initial=resource.name)
            self.fields[f'quantity_{resource.pk}'] = forms.IntegerField(initial=resource.quantity)

class ResourceForm(forms.ModelForm):

    class Meta:
        model = Resource
        fields = ['name', 'quantity']  # Add other fields if necessary

