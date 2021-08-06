"""gs117 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from school import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TemplateView.as_view(template_name='school/home.html'), name='blankhome'),
    path('home/', views.RedirectView.as_view(url='/'), name='abc'),
    # path('index/', views.RedirectView.as_view(url='/'), name='index'),
    path('index/', views.RedirectView.as_view(pattern_name='abc'), name='index'),
    #path('ojas/', views.RedirectView.as_view(url='https://www.ojas-it.com/'), name='go-to-ojas'),
    path('ojas1/', views.ojasRedirectView.as_view(), name='go-to-ojas'),

    path('home/<int:pk>/', views.newRedirectView.as_view(), name='geek'),
    path('<int:pk>/', views.TemplateView.as_view(template_name='school/home.html'), name='mindex'),

    # path('home/<slug:post>/', views.newRedirectView.as_view()),
    # path('<slug:post>/', views.TemplateView.as_view(template_name='school/home.html'), name='mindex'),
]
