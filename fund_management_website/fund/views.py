from django.shortcuts import render
from django.http import HttpResponse

#from fund.forms import RegisterForm
# Create your views here.

def index(request):
    	return HttpResponse("This is the index page")

def register(request):
	registered = False

	if request.method == 'POST':
		register_form = RegisterForm(data=request.POST)
		if register_form.is_valid():
			user = register_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print(register_form.errors)
	else:
		register_form = RegisterForm()
	return render(request,
		'fund/register.html',
		{'register_form':register_form,
		'registered':registered})