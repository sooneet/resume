from dataclasses import field
from pyexpat import model
from turtle import textinput
from . models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
            model = Contact
            fields = ['conatact_name', 'contact_email', 'contact_subject', 'contact_message']
            labels  = {
                'conatact_name':'Name', 
                'contact_email':'Email', 
                'contact_subject':'Subject', 
                'contact_message':'Message', 

                }
            widgets = {
            'conatact_name':forms.TextInput(attrs={'class':'form-control','id':'name'}),
            'contact_email':forms.EmailInput(attrs={'class':'form-control','id':'email'}),
            'contact_subject':forms.TextInput(attrs={'class':'form-control','id':'subject'}),
            'contact_message':forms.TextInput(attrs={'class':'form-control','id':'message'})
            }
