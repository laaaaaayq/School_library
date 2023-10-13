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
    path('backtoregister',views.backtoregister,name='backtoregister'),
    path('register',views.display1),
    path('login',views.login,name='login'),
    path('product',views.product,name='product'),
    path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('messagesend',views.message,name='messagesend'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('password',views.password,name='password'),
    path('product1/<int:id>',views.product1),
    path('library',views.library, name='library'),
    path('profile',views.profile,name='profile'),
    path('history',views.history,name='history'),
    path('user',views.user_history,name='user'),
    path('addbook',views.addbook),
    path('success',views.success),
    path('logout',views.logout,name='logout'),
    path('deletebook/<int:id>',views.deletebook,name='deletebook'),
    path('return/<int:id>',views.returnbook,name='return'),
    path('editbook/<int:id>',views.editbook, name='editbook'),
    path('search',views.search, name='search'),
    path('getbook',views.getbook, name='getbook'),
    path('nobook',views.nobook, name='nobook')
    # path('usersearch',views.usersearch, name='usersearch'),
    # path('editbookview',views.editbookview)
    # path('search',views.lib_search)
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)