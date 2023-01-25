from django import forms
from . models import ContactMe, Billing

class FormContact(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = '__all__'
        
class FormBilling(forms.ModelForm):
    class Meta:
        model = Billing
        fields = '__all__'
    