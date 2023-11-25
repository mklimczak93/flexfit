from django import forms

class StudioForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Studio