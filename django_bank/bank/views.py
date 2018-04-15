# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from bank.models import Profile,Transaction
#from article.models import Article, Comment
from django.http import HttpResponseRedirect
from forms import TransactionForm
from django.utils import timezone
from django.db.models import Max

# Create your views here.
def home(request):
    user = None
    if request.user.is_authenticated():
        username = request.user.username
        user = User.objects.get(username=username)
    return render_to_response('home.html',{'user': user})

def transfer(request):
    if request.method=="POST":
        f = TransactionForm(request.POST)
        if f.is_valid():
            recaccno = f.cleaned_data['receiver_accno']
            transpass = f.cleaned_data['transaction_password']
            amt = f.cleaned_data['amount']
            curruser = User.objects.get(username=request.user.username)
            balance = curruser.profile.balance
            transactionpass = curruser.profile.transaction_password
            receiver = Profile.objects.get(account_no=recaccno)
            if balance >= amt:
                if receiver is not None:
                     if transpass == transactionpass:
                         receiver.balance = receiver.balance + amt
                         receiver.save()
                         curruser.profile.balance = curruser.profile.balance - amt
                         curruser.save()
                         f.save()
                         iid = (Transaction.objects.all().aggregate(Max('id')))['id__max']
                         currtrans = Transaction.objects.get(id=iid)
                         currtrans.sender_accno = curruser.profile.account_no
                         currtrans.save()
                         return render_to_response('transfer_success.html')
        return render_to_response('transfer_fail.html')
    args = {}
    #args.update(csrf(request))

    args['f'] = TransactionForm()
    print args
    #return render_to_response('register.html', args)
    return render(request,'transfer.html',args)

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def transactions(request):
    args = {}
    args['transactions'] = Transaction.objects.all()
    curruser = request.user.username
    args['user'] = User.objects.get(username=curruser)
    return render(request, 'transactions.html', args)
