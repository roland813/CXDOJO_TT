from django import forms
from django.contrib.auth.forms import UserCreationForm

from app.models import UserData


class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData


class UserDataCreateForm(UserCreationForm):
    class Meta:
        model = UserData
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name")
