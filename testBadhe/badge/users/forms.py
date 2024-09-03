
from django.forms import ModelForm,Textarea,TextInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class SignUpForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(),widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Группа'}))
    fullname = forms.CharField(max_length=150, required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ФИО'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields =UserCreationForm.Meta.fields +  ('group', 'fullname')
