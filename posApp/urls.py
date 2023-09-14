from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('', views.home, name="home-page"),
    path('login', auth_views.LoginView.as_view(template_name = 'posApp/login.html',redirect_authenticated_user=True), name="login"),
    path('userlogin', views.login_user, name="login-user"),
    path('logout', views.logoutuser, name="logout"),
    path('category', views.category, name="category-page"),
    path('manage_category', views.manage_category, name="manage_category-page"),
    path('save_category', views.save_category, name="save-category-page"),
    path('delete_category', views.delete_category, name="delete-category"),
    path('products', views.products, name="product-page"),
    path('manage_products', views.manage_products, name="manage_products-page"),
    path('test', views.test, name="test-page"),
    path('save_product', views.save_product, name="save-product-page"),
    path('delete_product', views.delete_product, name="delete-product"),
    path('pos', views.pos, name="pos-page"),
    path('checkout-modal', views.checkout_modal, name="checkout-modal"),
    path('save-pos', views.save_pos, name="save-pos"),
    path('sales', views.salesList, name="sales-page"),
    path('receipt', views.receipt, name="receipt-modal"),
    path('delete_sale', views.delete_sale, name="delete-sale"),

    path('expenseCategory', views.expenseCategory, name='expenseCategory'),
    path('manage_expenseCategory', views.manage_expenseCategory, name="manage_expenseCategory"),
    path('saveExpenseCategory', views.saveExpenseCategory, name='saveExpenseCategory'),
    path('deleteExpenseCategory', views.deleteExpenseCategory, name="deleteExpenseCategory"),

    path('expenseProducts', views.expenseProducts, name="expenseProducts"),
    path('manage_expenseProducts', views.manage_expenseProducts, name="manage_expenseProducts"),
    path('save_expenseProduct', views.save_expenseProduct, name="save_expenseProduct"),
    path('delete_expenseProduct', views.delete_expenseProduct, name="delete_expenseProduct"),
    path('employees', views.employees, name="employee_page"),
    path('manage_employees', views.manage_employees, name="manage_employees_page"),
    path('save_employee', views.save_employee, name="save_employee_page"),
    path('delete_employee', views.delete_employee, name="delete_employee"),
    # path('view_employee', views.view_employee, name="view_employee-page"),
]