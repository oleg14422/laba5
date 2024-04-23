from django import forms

class sendTgMessageForm(forms.Form):
    message = forms.CharField(label = 'Введіть повідомлення')
    userId = forms.IntegerField(label = 'Введіть id користувача')