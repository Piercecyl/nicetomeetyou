"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from django.urls import path
from stock import views

router = DefaultRouter()
router.register(r'stock', views.StockViewSet)
app_name = 'accounts'

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='about'),
    path('crawler/', views.click_crawler),
    path('newsapi/', views.Get_news_List.as_view(), name='login'),
]


