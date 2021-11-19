from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView
from .models import *
from cart.forms import CartAddProductForm
from .forms import *


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def success_register(request):
    return render(request, 'success.html', context={
        'title': 'Заявка на регистрацию успешно оформлена',
        'description': 'Ожидайте подтверждения администрации. После подтверждения вам на указанную почту придут данные для входа',
    })


@login_required
def success_order(request):
    return render(request, 'success.html', context={
        'title': 'Заказ успешно оформлен',
        'description': 'Ожидайте звонка оператора для подтверждения заказа',
    })


@login_required
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available__gt=0)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'products.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


@login_required
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'product-card.html', {'product': product,
                                                 'cart_product_form': cart_product_form})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('shop:success_register')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def post(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.save()

            user.is_active = False
            user.save()

            return redirect('shop:success_register')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += 'text-center'
            return render(request, self.template_name, {'form': form})


class LoginUser(LoginView):
    authentication_form = LoginUserForm
    template_name = 'login.html'
    success_url = reverse_lazy('shop:home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('shop:home')


def logout_view(request):
    logout(request)
    return redirect('shop:home')


def user_orders(request):
    customer = User.objects.get(username=request.user)
    obj = Order.objects.filter(customer_username=customer.username)
    return render(request, 'orders.html', context={'obj': obj})


