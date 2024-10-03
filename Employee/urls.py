"""Employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',views.EmployeeCreateView.as_view(),name='Employe_create'),
    path('list/',views.EmployeListView.as_view(),name='employe_list'),
    path('details/<int:pk>/',views.EmployeDetailsView.as_view(),name='employe_detail'),
    path('delete/<int:pk>/remove',views.EmployeDeleteView.as_view(),name="Employe_delete"),
    path('update/<int:pk>/update',views.EmployeeUpdateView.as_view(),name="employe_update")


]
