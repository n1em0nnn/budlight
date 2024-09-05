from lib2to3.pgen2.tokenize import group

from .models import Badge

from django.forms import ModelForm, Textarea, TextInput, ModelChoiceField


class BadgeForm(ModelForm):
    class Meta:
        model = Badge
        fields = ['image','name','desc','cost']
        widgets={
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование значка'
            }),
            'desc': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            'cost': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость'
            })

        }