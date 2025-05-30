"""
URL configuration for crud1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from enroll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add_show,name="add_show"),
    path('delete/<int:id>/',views.delete_data,name="delete-data"),
    path('<int:id>/',views.update_data,name="updated-data"),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('javascriptvalid/',views.javascriptvalid,name='javascriptvalid'),
    path('send_email/',views.send_email,name='send_email'),
    path('send_otp/',views.send_sms,name='send_sms')

]
