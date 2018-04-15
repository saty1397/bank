"""django_bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django_bank.views import login, auth_view, logout, loggedin, invalid_login,register_user,register_success
#from django_bank.views import register_user,register_success,login
admin.autodiscover()

urlpatterns = [
    url(r'^bank/', include('bank.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/auth$', auth_view, name='auth_view'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^accounts/loggedin/$', loggedin, name='loggedin'),
    url(r'^accounts/invalid/$', invalid_login, name='invalid_login'),
    url(r'^accounts/register/$', register_user, name='register_user'),
    url(r'^accounts/register_success/$', register_success, name='register_success'),
]
