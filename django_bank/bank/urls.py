from django.conf.urls import url,include
from bank.views import home,transfer,logout

urlpatterns = [
    url(r'^home/$', home, name='home'),
    #url(r'^transactions/$', transactions, name='transactions'),
    url(r'^transfer/$', transfer, name='transfer'),
    url(r'^logout/$', logout, name='logout'),
]
