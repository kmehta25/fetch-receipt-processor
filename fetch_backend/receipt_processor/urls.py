from django.urls import include, path
from . import views

app_name = "receipts"

urlpatterns = [
    path('receipts/<int:pk>/points', views.ReceiptPointsView.as_view(), name = 'receipt_points'),
    path('receipts/process', views.ReceiptProcessView.as_view(), name = 'receipt_process'),
]