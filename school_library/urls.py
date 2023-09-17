"""
URL configuration for school_library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.display),
    path('register',views.display1),
    path('login',views.login),
    path('product',views.product),
    path('index',views.index),
    path('about',views.about),
    path('contact',views.contact),
    path('changepassword',views.changepassword),
    path('password',views.password),
    path('product1',views.product1),
    path('product2',views.product2),
    path('product3',views.product3),
    path('product4',views.product4),
    path('product5',views.product5),
    path('product6',views.product6),
    path('product7',views.product7),
    path('product8',views.product8),
    path('product9',views.product9),
    path('product10',views.product10),
    path('product11',views.product11),
    path('library',views.library),
    path('profile',views.profile),
    path('history',views.history)
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)