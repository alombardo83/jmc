from django import forms

from captcha.fields import CaptchaField

from core.widgets import BootstrapCaptchaTextInput

RATING = [
    (0, ''),
    (1, u'\uf005'),
    (2, u'\uf005\uf005'),
    (3, u'\uf005\uf005\uf005'),
    (4, u'\uf005\uf005\uf005\uf005'),
    (5, u'\uf005\uf005\uf005\uf005\uf005'),
]


class RatingForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur', max_length=100)
    rating = forms.IntegerField(label='Note', widget=forms.Select(choices=RATING))
    body = forms.CharField(label='Message', widget=forms.Textarea)
    captcha = CaptchaField(label='Captcha', widget=BootstrapCaptchaTextInput)
