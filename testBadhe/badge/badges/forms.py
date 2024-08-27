from .models import Badge

from django.forms import ModelForm,Textarea,TextInput

class BadgeForm(ModelForm):
    class Meta:
        model = Badge
        fields = ['name','desc','cost']

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