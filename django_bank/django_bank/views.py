from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.views.decorators import csrf
from forms import MyRegistrationForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Max
#from model import Profile
def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            users = form.save()
            users.refresh_from_db()
            users.profile.transaction_password = form.cleaned_data.get('transaction_password')
            users.profile.balance = 10000
            users.save()
            return HttpResponseRedirect('/accounts/register_success/')
    args = {}
    #args.update(csrf(request))

    args['form'] = MyRegistrationForm()
    print args
    #return render_to_response('register.html', args)
    return render(request,'register.html',args)

def register_success(request):
    #user = User.objects.get(article)
    iid = (User.objects.all().aggregate(Max('id')))['id__max']
    curracc = User.objects.get(id=iid)
    curracc.profile.account_no = iid+1000
    accno = iid+1000
    curracc.save()
    return render_to_response('register_success.html', {'account' : accno})

def login(request):
    c={}
    #c.update(csrf(request))
    return render(request,'login.html', c)

def auth_view(request):

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def initial(request):
    return render_to_response('initial.html')
