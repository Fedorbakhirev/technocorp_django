from django import forms

from shop.models import Order

PRODUCT_QTY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    qty = forms.TypedChoiceField(
        choices=PRODUCT_QTY_CHOICES,
        coerce=int, label='Количество',
        widget=forms.Select(attrs={'class': 'bg-x-gray w-10'}),
    )
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )


class OrderCreatingForm(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2',
        'autocomplete': 'off',
        'placeholder': 'Имя', }))
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2',
        'autocomplete': 'off',
        'placeholder': 'Фамилия', }))
    email = forms.EmailField(label='Эл. почта', widget=forms.EmailInput(attrs={
        'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2',
        'autocomplete': 'off',
        'placeholder': 'Эл. почта', }))
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2',
        'autocomplete': 'off',
        'placeholder': 'Номер телефона', }))
    address = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2',
        'autocomplete': 'off',
        'placeholder': 'Адрес', }))
    note = forms.CharField(label='Комментарий к заказу', widget=forms.Textarea(attrs={
        'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2',
        'autocomplete': 'off',
        'placeholder': 'Комментарий к заказу', }))

    class Meta:
        model = Order
        fields = ('name', 'surname', 'email', 'phone', 'address', 'note')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2'}),
            'surname': forms.TextInput(attrs={
                'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2'}),
            'email': forms.EmailInput(attrs={
                'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2'}),
            'phone': forms.TextInput(attrs={
                'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2'}),
            'address': forms.TextInput(attrs={
                'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2'}),
            'note': forms.Textarea(attrs={
                'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2'}),
        }