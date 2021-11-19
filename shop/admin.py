from django import forms

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import *

UserAdmin.list_display = ['username', 'first_name', 'last_name', 'email', 'is_active']
UserAdmin.list_editable = ['is_active']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['id', 'title', 'category', 'price', 'available', 'image_show']
    list_filter = ['available', 'price']
    list_editable = ['available', 'price']
    list_display_links = ['id', 'title']

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60'/>".format(obj.image.url))
        return None

    image_show.short_description = 'Фото'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_username', 'address', 'email', 'phone', 'created_at']
    list_filter = ['customer_username']
    list_display_links = ['id', 'customer_username']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
