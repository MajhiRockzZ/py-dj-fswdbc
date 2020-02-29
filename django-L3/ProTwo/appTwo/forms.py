from django import forms
from appTwo.models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        field = '__all__'
