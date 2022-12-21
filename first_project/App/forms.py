from django import forms

class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField(required=False)
    email = forms.EmailField(required=False)