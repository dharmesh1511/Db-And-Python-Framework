"""
URL configuration for crud1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_doc/',views.add_doc,name='add_doc'),
    path('delete/<int:id>/',views.delete_data,name="delete-data"),
    path('<int:id>/',views.update_data,name="updated-data"),



#login logout url

    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('javascript_validation/', views.javascript_validation, name='javascript_validation'),
    
    path('send_sms/', views.send_sms, name='send_sms'),


# ajex crud
    path('ajaxcrud/', views.item_list, name='item_list'),
    path('create/', views.item_create, name='item_create'),
    path('update/<int:pk>/', views.item_update, name='item_update'),
    path('ajaxcrud/delete/<int:pk>/', views.item_delete, name='item_delete'),
    path('accounts/', include('allauth.urls')),

]
