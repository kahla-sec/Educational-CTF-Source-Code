from django import forms
class InputForm(forms.Form):
    Input=forms.CharField(label="Your link",max_length=100)