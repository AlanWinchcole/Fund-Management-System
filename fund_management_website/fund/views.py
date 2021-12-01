from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
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
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print(user_form.errors)
	else:
		user_form = UserForm()
	return render(request,
		'fund/register.html',
		{'user_form':user_form,
		'registered':registered})

def login(request):
	# if request.method == 'POST':
	# 	username = request.POST.get('username')
	# 	password = request.POST.get('password')
	# 	user = authenticate(username=username, password=password)
	# 	if user:
	# 		if user.is_active:
	# 			login(request, user)
	# 			return render(request,'fund/application.html')
	# 		else:
	# 			return HttpResponse("Your account is disabled.")
	# 	else:
	# 		print("Invalid login details: {0}, {1}".format(username, password))
	# 		return HttpResponse("Invalid login details supplied.")
	# else:
	# 	user_form = UserForm()
	# 	return render(request, 'fund/login.html', {'user_form':user_form})
	if request.user.is_authenticated:
		return redirect(reverse('fund:application'))
	if request.method == 'POST':
		user_form = AuthenticationForm(request=request,data = request.POST)

		if user_form.is_valid():
			login(request,user_form.get_user())
			return redirect(reverse('fund:application'))
		else:
			print(user_form.errors)

	else:
		user_form = AuthenticationForm()
	return render(request,'fund/login.html', {'user_form':user_form})



def dashboard(request):
	if request== 'POST':
		application_form = ApplicationForm(request.POST)
		if application_form.is_valid():
			application_form.save()
			HttpResponse("Yay your application has been submitted.")
		else:
			print(application_form.errors)
	else:
		application_form = ApplicationForm()
		return render(request,'fund/application.html', {'ApplicationForm':application_form})






