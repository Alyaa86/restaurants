"""foodhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from restaurants import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants/', views.list, name="restaurant_list"),
    path('details/<int:y>/', views.detail, name="restaurant_detail"),
    path('restaurant_form/', views.create, name="restaurant_form"),
    path('update_form/<int:restaurant_id>/', views.update, name="update_form"),
    path('delete/<int:restaurant_id>/', views.delete, name="delete"),
    path('create/<int:restaurant_id>/', views.create_item, name="item_form"),
    path('favourite/<int:x_id>/', views.favourite, name="favourite"),
    path('login/', views.user_login, name="login"),
    path('signup/', views.signup, name="sign_up"),
    path('logout/', views.log_out, name="logout"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)