from django import forms


class CodeMethodForm(forms.Form):
    code = forms.CharField()

