from django.urls import path
from fund import views
from django.contrib.auth.views import LogoutView
from fund_management_website import settings

app_name = "fund"

urlpatterns = [
    path("", views.login, name = "index"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name = "login"),
    path("application/", views.dashboard, name = "application"),
    path("update_application/<int:id>", views.updateApplication, name = "update_application"),
    path("welcome/", views.welcome, name = "welcome"),
    #path("logout/", views.logout, name= "logout")
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('info/', views.info, name="info"),

]
