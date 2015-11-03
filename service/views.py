from django.shortcuts import render
from service.models import Client,Finance 
from django.shortcuts import render 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required(login_url='/login/')
def client_home(request):
	clients = Client.objects.all()
	user = User.objects.all()
	context_dict = {'clients':clients,'user':user}
	return render(request,'client/client-home.html', context_dict)

@login_required(login_url='/login/')
def finance_home(request):
	products = Finance.objects.all()
	context_dict = {'products':products}
	return render(request,'client/finance-home.html',context_dict)


@login_required(login_url='/login/')
def marketing_home(request):
	finance_products = Finance.objects.all()
	client_products = Client.objects.all()
	context_dict = {'finance_products':finance_products,'client_products':client_products}
	return render(request,'client/marketing-home.html',context_dict)


def login_view(request):
	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				if username[0]=="c":
					return HttpResponseRedirect('/service/client/')
				elif username[0]=="f":
					return HttpResponseRedirect('/service/finance/')
				else:
					return HttpResponseRedirect('/service/marketing/')
			else:
				return HttpResponse("Your account is disabled")
		else:
			return HttpResponse("Invalid login details")
	else:
		return render(request,'client/login.html',{})


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/login/')
