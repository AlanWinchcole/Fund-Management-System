from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.urls import reverse
from fund.forms import *
from django.views.decorators.csrf import csrf_exempt
from fund.models import *
import json


# Create your views here.

def index(request) :
    return HttpResponse("This is the index page")


def register(request) :
    registered = False
    if request.method == 'POST' :
        user_form = UserForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and user_profile_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_profile_form.save(commit=False)
            profile.user = user

            profile.save()
            registered = True
        else :
            print(user_form.errors)
    else :
        user_form = UserForm()
        user_profile_form = UserProfileForm()
    return render(request,
                  'fund/register.html',
                  { 'user_form' :user_form,
                    'user_profile_form' :user_profile_form,
                    'registered' :registered })


def user_login(request) :
    if request.user.is_authenticated :
        return redirect(reverse('fund:dashboard'))
    if request.method == 'POST' :
        user_form = AuthenticationForm(request=request, data=request.POST)

        if user_form.is_valid() :
            login(request, user_form.get_user())
            return redirect(reverse('fund:dashboard'))
        else :
            print(user_form.errors)

    # else:
    # user_form = AuthenticationForm()
    return render(request, 'fund/login.html')  # {'user_form':user_form})


@login_required
def user_logout(request) :
    logout(request)

def reviewApplication(request, id):
    application = ApplicationData.objects.get(id=id)
    review_form = ReviewForm()
    if request.method == 'POST' :
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.application = application
            review.user = request.user
            #print(review.score())

            review.save()
            review.application.save()

            return redirect("fund:dashboard")
        else:
            print(review_form.errors, app_reviewd_form.errors)
    else:
        return render(request, 'fund/review.html', { 'form' :review_form,})



def application(request) :
    user = request.user
    print(user)
    application_form = ApplicationForm()
    if request.method == 'POST' :
        application_form = ApplicationForm(request.POST)
        if application_form.is_valid() :
            print("form is valid")
            application = application_form.save(commit=False)
            application.user = user
            print(application.user)
            application.save()
            return redirect('fund:dashboard')
        else :
            print(application_form.errors)
    else :

        return render(request, 'fund/application.html', { 'form' :application_form })


# id is the application id
def updateApplication(request, id) :
    applicationObj = ApplicationData.objects.get(id=id)
    application_form = ApplicationForm(instance=applicationObj)

    if request.method == 'POST' :
        application_form = ApplicationForm(request.POST, instance=applicationObj)
        if application_form.is_valid() :
            print("form is valid")
            application_form.save()
            return redirect('fund:dashboard')
        else :
            print(application_form.errors)
    else :
        return render(request, 'fund/application.html', { 'form' :application_form })


def budgetProfile(request) :
    items = BudgetItems.objects.all()
    # items = SubBudgetProfile.objects.all()
    return render(request, "fund/budgetProfile.html", { "items" :items })


def SpendProfile(request) :
    items = SpendingItems.objects.all()
    # spendObj = SpendingItems.objects.get(id=id)
    # item =  SpendingItems(request.POST, instance=spendObj)
    # item.save()
    # headings = BudgetItems.objects.all()
    return render(request, "fund/SpendProfile.html", { "items" :items })


@csrf_exempt
def addItem(request) :
    heading = request.POST.get("heading")
    ID = request.POST.get("ID")
    item_name = request.POST.get("item_name")
    description = request.POST.get("description")
    budget_allocation = request.POST.get("budget_allocation")

    try :

        heading = SubBudgetProfile(heading=heading)
        heading.save()
        item = BudgetItems(ID=ID, heading=heading, item_name=item_name, description=description,
                           budget_allocation=budget_allocation)
        item.save()
        spend_items = SpendingItems(ID=ID, heading=heading, item_name=item_name, description=description,
                                    budget_allocation=budget_allocation)
        spend_items.save()
        item_data = { "heading" :item.ID, "error" :False, "errorMessage" :"Item Added Successfully" }
        return JsonResponse(item_data, safe=False)
    except :
        item_data = { "error" :True, "errorMessage" :"Failed to add item" }
        return JsonResponse(item_data, safe=False)


@csrf_exempt
def addItemSpendProfile(request) :
    heading = request.POST.get("heading")
    ID = request.POST.get("ID")
    item_name = request.POST.get("item_name")
    description = request.POST.get("description")
    money_spent = request.POST.get("money_spent")

    try :

        spend_items = SpendingItems(ID=ID, heading=heading, item_name=item_name, description=description,
                                    money_spent=money_spent)
        spend_items.save()
        item_data = { "heading" :spend_items.ID, "error" :False, "errorMessage" :"Item Added Successfully" }
        return JsonResponse(item_data, safe=False)
    except :
        item_data = { "error" :True, "errorMessage" :"Failed to add item" }
        return JsonResponse(item_data, safe=False)


@csrf_exempt
def saveItem(request) :
    data = request.POST.get("data")
    dict_data = json.loads(data)
    try :
        for dic_single in dict_data :
            heading = SubBudgetProfile(heading=dic_single['heading'])
            heading.save()
            # item2 = BudgetItems(heading=heading.heading)
            # item2.save()
            # item_heading = SubBudgetProfile.objects.get(heading=dic_single['heading'])
            item = BudgetItems.objects.get(ID=dic_single['ID'])
            # item.heading=item_heading.heading
            item.item_name = dic_single['item_name']
            item.description = dic_single['description']
            item.budget_allocation = dic_single['budget_allocation']
            item.save()
        item_data = { "error" :False, "errorMessage" :"Items Updated Successfully" }
        return JsonResponse(item_data, safe=False)
    except :
        item_data = { "error" :True, "errorMessage" :"Failed to Update Data" }
        return JsonResponse(item_data, safe=False)


@csrf_exempt
def saveItemSpendProfile(request) :
    data = request.POST.get("data")
    dict_data = json.loads(data)
    try :
        for dic_single in dict_data :
            # heading=SubBudgetProfile(heading=dic_single['heading'])
            # heading.save()
            # item2 = BudgetItems(heading=heading.heading)
            # item2.save()
            # item_heading = SubBudgetProfile.objects.get(heading=dic_single['heading'])
            item = SpendingItems.objects.get(ID=dic_single['ID'])
            item.heading = dic_single['heading']
            item.item_name = dic_single['item_name']
            item.description = dic_single['description']
            item.evidence = dic_single['evidence']
            item.money_spent = dic_single['money_spent']
            item.save()
        item_data = { "error" :False, "errorMessage" :"Items Updated Successfully" }
        return JsonResponse(item_data, safe=False)
    except :
        item_data = { "error" :True, "errorMessage" :"Failed to Update Data" }
        return JsonResponse(item_data, safe=False)


@csrf_exempt
def deleteItem(request) :
    ID = request.POST.get("ID")
    try :
        item = BudgetItems.objects.get(ID=ID)
        item.delete()
        item_data = { "error" :False, "errorMessage" :"Deleted Successfully" }
        return JsonResponse(item_data, safe=False)
    except :
        item_data = { "error" :True, "errorMessage" :"Failed to Delete Data" }
        return JsonResponse(item_data, safe=False)


def welcome(request) :
    return render(request, 'fund/info.html')


def info(request) :
    return render(request, 'fund/info.html')


def base(request) :
    return render(request, 'fund/base.html')


def dashboard(request) :
    username = request.user.username
    full_name = request.user.get_full_name()
    email = request.user.email
    if request.user.is_superuser :
        admin = True
        users = get_user_model()
        user_list = users.objects.all()
        completed_applications = ApplicationData.objects.filter(application_complete=True).order_by(
            'date_of_application')
        return render(request, 'fund/dashboard.html',
                      context={ 'completed_applications' :completed_applications,
                                "username" :username, "full_name" :full_name,
                                "email" :email, "user_list" :user_list, 'admin' :admin })
    else :
        completedApplications = ApplicationData.objects.filter(user=request.user, application_complete=True)
        incompleteApplications = ApplicationData.objects.filter(user=request.user, application_complete=False)
        contact = UserProfile.objects.get(user=request.user).contact_number
        return render(request, 'fund/dashboard.html', context={ 'completed_applications' :completedApplications,
                                                                'incomplete_applications' :incompleteApplications,
                                                                "username" :username, "full_name" :full_name,
                                                                "email" :email, "contact" :contact,
                                                                })


from django.contrib.auth.decorators import user_passes_test

def view_review(request, id):
    admin = True if request.user.is_superuser else False
    review = Review.objects.get(id=id)
    review_form = ReviewForm(instance=review)
    return render(request, 'fund/review_view.html', {'review':review,'review_form':review_form})

@user_passes_test(lambda u :u.is_superuser)
def user_profile(request, username) :
    users = get_user_model()
    user = users.objects.get(username=username)
    print(user)
    if user.is_superuser :
        admin = True
    else :
        admin = False
    completed_applications = None
    username = user.username
    full_name = user.get_full_name()
    email = user.email
    contact = None
    if not admin :
        contact = UserProfile.objects.get(user=user).contact_number
        completed_applications = ApplicationData.objects.filter(user=user, application_complete=True)
        print(completed_applications)

    data = { "username" :username, "full_name" :full_name, "email" :email,
             "completed_applications" :completed_applications, 'contact' :contact, 'admin' :admin }
    return render(request, 'fund/user_profile.html', context=data)


def applicationIntroduction(request) :
    return render(request, 'fund/application_introduction.html')
