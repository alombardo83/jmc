from django import forms

from captcha.fields import CaptchaField

from .widgets import BootstrapCaptchaTextInput


class ContactForm(forms.Form):
    first_name = forms.CharField(label='Prénom', max_length=50)
    last_name = forms.CharField(label='Nom', max_length=50)
    email_address = forms.EmailField(label='Adresse email', max_length=150)
    message = forms.CharField(label='Message', widget=forms.Textarea, max_length=2000)
    captcha = CaptchaField(label='Captcha', widget=BootstrapCaptchaTextInput)
