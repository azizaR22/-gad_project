from django.urls import path
from . import views
from .views import Customer_detail, Customer_update, Customer_list

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutuser, name="logout"),
    path("register/", views.registration, name="register"),
    path("", views.home, name="home"),
    path("viewcust/", Customer_list.as_view(), name="view-cust"),
    path("add-cust/", views.add_custom, name="add-cust"),
    path(
        "customer-detail/<int:pk>/", Customer_detail.as_view(), name="customer-detail"
    ),
    path(
        "customer-update/<int:pk>/", Customer_update.as_view(), name="customer-update"
    ),
]
