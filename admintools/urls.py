from django.urls import path
from .views import *

app_name = 'admintools'

urlpatterns = [
    path('', admintools, name='admintools'),
    path('orderreport/', order_report, name='orderreport')
]
