from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('export-pdf/', views.export_to_pdf, name='export_to_pdf'),
]
