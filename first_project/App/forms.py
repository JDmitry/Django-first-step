from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Name", help_text="Enter the name")
    num = forms.CharField(label="Num", help_text="Enter the num", initial=0)
    comment = forms.CharField(label="Comments", widget=forms.Textarea)
    field_order = ["name", "num", "comment"]