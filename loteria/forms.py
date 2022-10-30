# -*- coding: utf-8 -*-
from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'size':'35'}))
    email = forms.EmailField()
    asunto = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'size':'35'}))
    mensaje = forms.CharField(max_length=500, widget=forms.Textarea())
    

    


