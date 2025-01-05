from django import forms
from .models import SesKayit

class SesKayitForm(forms.ModelForm):
    class Meta:
        model = SesKayit
        fields = ['isim', 'ses_dosyasi']
