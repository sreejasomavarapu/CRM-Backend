from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   
    path('', views.home,name='home'),
    path('customer/', views.customer),
    path('products/', views.products),
    path('order/<str:pk>', views.order, name='order'),
    path('create-order', views.create_order, name='create-order'),
    path('delete-order/<str:pk>', views.delete_order, name='delete-order'),
    path('update-order/<str:pk>', views.update_order, name='update-order'),
    path('customer-create-order/<str:pk>', views.customer_create_order, name='customer-create-order'),
    path('register/', views.register, name='register'),
    path('logout/',auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login')
]