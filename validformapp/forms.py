from django import forms


class NameForm(forms.Form):  # Форма от встроеного класса Form
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
