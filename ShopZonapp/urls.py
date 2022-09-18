"""shopinglyX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ProductView.as_view(),name='home'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

















