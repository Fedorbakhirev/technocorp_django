from django import forms
from django.forms import DateInput

from shop.models import Order


class OrderReport(forms.Form):
    from_date = forms.DateField(label='Дата начала', widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2',
        'autocomplete': 'off',
        'placeholder': 'Дата окончания', }))
    to_date = forms.DateField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2',
        'autocomplete': 'off',
        'placeholder': 'Дата окончания', }))

    class Meta:
        fields = ['from_data', 'to_data']
        widgets = {
            'from_date': forms.DateInput(attrs={'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2'}),
            'to_date': forms.DateInput(attrs={
                'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2'}),
        }