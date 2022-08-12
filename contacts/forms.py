from django import forms
from contacts.models import Contacts


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs= {'class':'form-control' }),
            'countryCode': forms.NumberInput(attrs= {'class': 'form-control'}),
            'contactNo': forms.NumberInput(attrs= {'class': 'form-control'}),
        'email': forms.EmailInput(attrs= {'class': 'form-control'}),
        }