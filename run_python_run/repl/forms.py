from django import forms


class CodeRunForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea())
