
from django.forms import ModelForm,Textarea,TextInput
from django import forms
from .models import CompModel,CompLevel, Result


class CompCreateForm(ModelForm):
    name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}))
    level = forms.ModelChoiceField(required=False,queryset=CompLevel.objects.all(), empty_label="Не выбран уровень",widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Группа'}))
    city = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Город'}))
    org = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Организатор'}))
    fcdo = forms.BooleanField(required=False)
    result = forms.ModelChoiceField(required=False,queryset=Result.objects.all(),
                                    empty_label="Не выбран результат",
                                    widget=forms.Select(
                                        attrs={'class': 'form-control'}))
    class Meta:
        model = CompModel
        fields = ['name','level','city','org','fcdo','result']


