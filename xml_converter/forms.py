from django import forms


class FileForm(forms.Form):
    title = forms.CharField(label='Name', max_length=50)
    file = forms.FileField()
