from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect

from admintools.forms import OrderReport
from shop.models import Order


@staff_member_required
def order_report(request):
    form = OrderReport(request.POST)
    if form.is_valid():
        obj = Order.objects.filter(created_at__gte=form.cleaned_data['from_date'], created_at__lte=form.cleaned_data['to_date'])
        return render(request, 'order_report.html', {'form': form, 'obj':obj})
    else:
        return render(request, 'order_report.html', {'form': form})


@staff_member_required
def admintools(request):
    return render(request, 'admintools.html')
