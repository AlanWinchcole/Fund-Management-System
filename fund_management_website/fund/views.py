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

def user_login(request):
	if request.user.is_authenticated:
		return redirect(reverse('fund:dashboard'))
	if request.method == 'POST':
		user_form = AuthenticationForm(request=request,data = request.POST)

		if user_form.is_valid():
			login(request,user_form.get_user())
			return redirect(reverse('fund:dashboard'))
		else:
			print(user_form.errors)

	else:
		user_form = AuthenticationForm()
	return render(request,'fund/login.html', {'user_form':user_form})


@ login_required
def user_logout(request):
	logout(request)

def application(request):
	application_form = ApplicationForm()
	if request.method == 'POST':
		application_form = ApplicationForm(request.POST)
		if application_form.is_valid():
			print("form is vali")
			application_form.save()
			return redirect('fund:dashboard')
		else:
			print(application_form.errors)
	else:

		return render(request,'fund/application.html', {'form':application_form})

# id is the application id
def updateApplication(request, id):
	applicationObj = ApplicationData.objects.get(id=id)
	application_form = ApplicationForm(instance = applicationObj)

	if request.method == 'POST':
		application_form = ApplicationForm(request.POST, instance=applicationObj)
		if application_form.is_valid():
			print("form is valid")
			application_form.save()
			return redirect('fund:dashboard')
		else:
			print(application_form.errors)
	else:
		return render(request,'fund/application.html', {'form':application_form})

def budgetProfile(request):
	items = BudgetItems.objects.all()
	#headings = SubBudgetProfile.objects.all()
	return render(request,"fund/budgetProfile.html",{"items":items})

def SpendProfile(request):
	items = SpendingItems.objects.all()
	return render(request, "fund/SpendProfile.html",{"items":items})
	
@csrf_exempt
def addItem(request):
    heading=request.POST.get("heading")
    ID=request.POST.get("ID")
    item_name=request.POST.get("item_name")
    description=request.POST.get("description")
    budget_allocation=request.POST.get("budget_allocation")

    try:
        
        heading = SubBudgetProfile(heading=heading)
        heading.save()
        item = BudgetItems(ID=ID,heading=heading,item_name=item_name,description=description,budget_allocation=budget_allocation)
        item.save()
        item_data={"heading":item.ID,"error":False,"errorMessage":"Item Added Successfully"}
        return JsonResponse(item_data,safe=False)
    except:
        item_data={"error":True,"errorMessage":"Failed to add item"}
        return JsonResponse(item_data,safe=False)

@csrf_exempt
def saveItem(request):
	data=request.POST.get("data")
	dict_data=json.loads(data)
	try:
		for dic_single in dict_data:
			heading=SubBudgetProfile(heading=dic_single['heading'])
			heading.save()
			#item2 = BudgetItems(heading=heading.heading)
			#item2.save()
			#item_heading = SubBudgetProfile.objects.get(heading=dic_single['heading'])
			item=BudgetItems.objects.get(ID=dic_single['ID'])
			#item.heading=item_heading.heading
			item.item_name=dic_single['item_name']
			item.description=dic_single['description']
			item.budget_allocation=dic_single['budget_allocation']
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
        item=BudgetItems.objects.get(ID=ID)
        item.delete()
        item_data={"error":False,"errorMessage":"Deleted Successfully"}
        return JsonResponse(item_data,safe=False)
    except:
        item_data={"error":True,"errorMessage":"Failed to Delete Data"}
        return JsonResponse(item_data,safe=False)

def welcome(request):
	return render(request,'fund/info.html')

def info(request):
	return render(request,'fund/info.html')

def base(request):
	return render(request,'fund/base.html')

def dashboard(request):
	allApplications = ApplicationData.objects.all()
	username  =request.user.username
	full_name = request.user.get_full_name()
	email = request.user.email
	return render(request, 'fund/dashboard.html', context={'applications':allApplications,"username":username, "full_name":full_name, "email":email})




