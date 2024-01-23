from django import forms
from django.contrib.auth import login
from django.contrib.auth import authenticate
import ipdb


class LoginForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.request = request
        self.fields["email"] = forms.EmailField()
        self.fields["password"] = forms.CharField()

    def is_valid(self):
        valid = super(LoginForm, self).is_valid()
        if valid:
            user = authenticate(
                username=self.cleaned_data["email"],
                password=self.cleaned_data["password"],
            )
            if user:
                login(self.request, user)
            else:
                valid = False
        return valid
