from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login

from CRM import models



# Create your views here.

@login_required
def index(request):

    return render(request, 'crm/index.html')



def acc_login(request):


    if request.method == 'POST':
        print(request.POST)

        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))

        if user is not None:
            # pass authentication

            login(request,user)
            return HttpResponseRedirect('/')


        else:
            login_error = 'Wrong username or password !!!'
            return render(request, 'crm/login.html', {'login_error':login_error})

    return render(request, 'crm/login.html')





#CRM 学员管理系统



def dashboard(request):

    return render(request, 'crm/dashboard.html')



def customers(request):

    customers_list = models.Customer.objects.all()
    return render(request,'crm/customers.html',{'customers_list':customers_list})
