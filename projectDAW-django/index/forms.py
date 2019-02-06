# make sure this is at the top if it isn't already
from django import forms

# our new form
class ContactForm(forms.Form):
    nombre = forms.CharField(required=True)
    correo = forms.EmailField(required=True)
    asunto = forms.CharField(required=True)
    mensaje = forms.CharField(
        required=True,
        widget=forms.Textarea
    )