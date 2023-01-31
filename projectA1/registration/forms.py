from django.contrib.auth.models import User
from django.contrib.contenttypes import forms


class UserForm(forms.ModelForm):
    password = forms.CharField()
    class Meta():
        model = User
        fields = ('username','password','email')