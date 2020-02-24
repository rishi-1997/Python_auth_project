from django import forms
from django.contrib.auth.models import User

class sign_up_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']

