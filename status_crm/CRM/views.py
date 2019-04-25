from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from CRM import models,forms






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


    #新版写法:https://docs.djangoproject.com/en/2.2/topics/pagination/
    paginator = Paginator(customers_list,2)
    page = request.GET.get('page')
    customers_obj = paginator.get_page(page)


    # 旧版写法：https://docs.djangoproject.com/en/1.9/topics/pagination/
    # try:
    #     customers_obj =paginator.page('page')
    #
    # except PageNotAnInteger:
    #     customers_obj = paginator.page(1)
    #
    # except EmptyPage:
    #     customers_obj = paginator.page(paginator.num_pages


    return render(request,'crm/customers.html',{'customers_list':customers_obj})


def customer_detail(request,customer_id):

    customer_obj = models.Customer.objects.get(id=customer_id)
    form = forms.CustomerModelForm()


    return render(request,'crm/customer_detail.html',{"customer_from":form})