from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from fund.forms import UserForm
from fund.forms import ApplicationForm
from django.views.decorators.csrf import csrf_exempt
from fund.models import *
import json


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



def application(request):
	application_form = ApplicationForm()
	if request.method == 'POST':
		application_form = ApplicationForm(request.POST)
		if application_form.is_valid():
			print("form is vali")
			application_form.save()
			return HttpResponse("Yay your application has been submitted.")
		else:
			print(application_form.errors)
	else:

		return render(request,'fund/application.html', {'ApplicationForm':application_form})

# id is the application id
def updateApplication(request, id):
	application = ApplicationData.objects.get(id=id)
	application_form = ApplicationForm(instance = application)
	if request.method == 'POST':
		application_form = ApplicationForm(request.POST, instance = application)
		if application_form.is_valid():
			print("form is vali")
			application_form.save()
			return HttpResponse("Yay your application has been submitted.")
		else:
			print(application_form.errors)
	else:
		return render(request,'fund/application.html', {'ApplicationForm':application_form})

def budgetProfile(request):
	items = BudgetProfile.objects.all()
	return render(request,"fund/budgetProfile.html",{"items":items})

@csrf_exempt
def addItem(request):
    heading=request.POST.get("heading")
    description=request.POST.get("description")
    totalCost=request.POST.get("totalCost")

    try:
        item=BudgetProfile(heading=heading,description=description,totalCost=totalCost)
        item.save()
        item_data={"ID":item.ID,"error":False,"errorMessage":"Item Added Successfully"}
        return JsonResponse(item_data,safe=False)
    except:
        item_data={"error":True,"errorMessage":"Failed to Item Student"}
        return JsonResponse(item_data,safe=False)

@csrf_exempt
def saveItem(request):
	data=request.POST.get("data")
	dict_data=json.loads(data)
	try:
		for dic_single in dict_data:
			item=BudgetProfile.objects.get(ID=dic_single['ID'])
			item.heading=dic_single['heading']
			item.description=dic_single['description']
			item.totalCost=dic_single['totalCost']
			item.save()
		item_data={"error":False,"errorMessage":"Items Updated Successfully"}
		return JsonResponse(item_data,safe=False)
	except:
		item_data={"error":True,"errorMessage":"Failed to Update Data"}
		return JsonResponse(item_data,safe=False)

@csrf_exempt
def deleteItem(request):
    ID=request.POST.get("ID")
    try:
        item=BudgetProfile.objects.get(ID=ID)
        item.delete()
        item_data={"error":False,"errorMessage":"Deleted Successfully"}
        return JsonResponse(item_data,safe=False)
    except:
        item_data={"error":True,"errorMessage":"Failed to Delete Data"}
        return JsonResponse(item_data,safe=False)

def welcome(request):
	return render(request,'fund/welcome.html')

@ login_required
def log_out(request):
	logout(request)

def info(request):
	return render(request,'fund/info.html')

def base(request):
	return render(request,'fund/base.html')

def test(request):
	return render(request,'fund/test.html')

def dashboard(request):
	return render(request, 'fund/dashboard.html')




