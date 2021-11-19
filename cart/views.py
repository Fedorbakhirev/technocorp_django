from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

import shop.models
from shop.models import *
from .cart import Cart
from .forms import CartAddProductForm, OrderCreatingForm


@login_required()
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        form.qty = 0
        cd = form.cleaned_data
        cart.add(product=product,
                 qty=cd['qty'],
                 update_qty=cd['update'])
    return redirect('cart:cart_detail')


@login_required()
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


@login_required()
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['updated_qty_form'] = CartAddProductForm(initial={'qty': item['qty'], 'update': True})
    return render(request, 'cart.html', {'cart': cart})


class CreateOrder(LoginRequiredMixin, CreateView):
    form_class = OrderCreatingForm
    template_name = 'order.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заказ создан'
        return context

    def post(self, request, *args, **kwargs):
        form = OrderCreatingForm(request.POST)
        customer = User.objects.get(username=request.user)
        cart = Cart(request)
        if form.is_valid():
            obj = form.save()
            obj.customer_username = str(customer)
            for item in cart:
                obj.products += f"{item['product'].title} {str(item['qty'])} шт.\n"
            obj.price = cart.get_total_price()
            obj.save()
            cart.clear()
            return redirect('shop:success_order')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += 'text-center'
            return render(request, self.template_name, {'form': form})
