from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from fund.forms import UserForm
from fund.forms import ApplicationForm
# Create your views here.

def index(request):
    	return HttpResponse("This is the index page")

def register(request):
	registered = False

	if request.method == 'POST':
		register_form = UserForm(data=request.POST)
		if register_form.is_valid():
			user = register_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print(register_form.errors)
	else:
		register_form = UserForm()
	return render(request,
		'fund/register.html',
		{'register_form':register_form,
		'registered':registered})

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		username = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'fund/login.html', {})






