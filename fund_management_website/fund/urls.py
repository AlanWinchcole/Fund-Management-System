"""Define the urls for html files"""

from django.urls import path
from django.contrib.auth.views import LogoutView
from fund import views
from fund_management_website import settings

app_name = "fund"

urlpatterns = [
    path("", views.user_login, name = "index"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name = "login"),
    path("apply/", views.application, name = "application"),
    path("update_application/<int:id>", views.updateApplication, name = "update_application"),
    path("budget_profile/",views.budgetProfile, name = "budget_profile"),
    path('add_item/', views.addItem,name="add_item"),
    path('add_item_spend/', views.addItemSpendProfile,name="add_item_spend"),
    path('save_item/', views.saveItem,name="save_item"),
    path('save_item_spend/', views.saveItemSpendProfile,name="save_item_spend"),
    path('delete_item/', views.deleteItem,name="delete_item"),
    path("welcome/", views.welcome, name = "welcome"),
    #path("logout/", views.logout, name= "logout")
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('welcome/', views.info, name="welcome"),
    path('base/', views.base, name="base"),
    path('dashboard/', views.dashboard, name ="dashboard"),
    path('budget_profile/', views.budgetProfile, name ="budget_profile"),
    path('spend_profile/', views.SpendProfile, name ="spend_profile"),
    path("application_introduction/", views.applicationIntroduction, name = "application_introduction"),
    path("user_profile/<str:username>", views.user_profile, name = "user_profile"),
    path("view_application_status/<int:id>", views.view_application_status, name="view_application_status"),
    path("add_comment/<int:id>", views.add_comment, name= "add_comment"),
    path("review/<int:id>", views.reviewApplication, name="review_application"),
    path("reviews/", views.reviews, name="reviews"),
    path("view_review/<int:id>", views.view_review, name="view_review"),
    path("update_review/<int:id>", views.updateReview, name="update_review"),
]
