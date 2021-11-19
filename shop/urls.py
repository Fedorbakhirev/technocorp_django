from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('products/<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('contacts/', contacts, name='contacts'),
    path('success/', success_register, name='success_register'),
    path('successorder/', success_order, name='success_order'),
    path('orders/', user_orders, name='user_orders')
]
