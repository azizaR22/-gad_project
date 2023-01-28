from django.shortcuts import render, redirect
from .models import Customer
from .forms import Customerform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


# Create your views here.


def loginPage(request):
    authenticationForm = AuthenticationForm()
    if request.method == "POST":
        authenticationForm = AuthenticationForm(request, data=request.POST or None)
        if authenticationForm.is_valid():
            username = authenticationForm.cleaned_data["username"]
            password = authenticationForm.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user=user)
                return redirect("home")
    context = {"authenticationForm": authenticationForm}
    return render(request, "base/login.html", context)


@login_required(login_url="login")
def home(request):
    context = {}
    return render(request, "base/home.html", context)


@login_required(login_url="login")
def logoutuser(request):
    if not request.user.is_authenticated:
        return redirect("login")
    logout(request)
    return redirect("login")


def registration(request):
    usercreationform = UserCreationForm()
    if request.method == "POST":
        usercreationform = UserCreationForm(request.POST or None)
        if usercreationform.is_valid():
            username = usercreationform.cleaned_data["username"]
            password = usercreationform.cleaned_data["password1"]
            usercreationform = usercreationform.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user=user)
                return redirect("home")

    context = {"usercreationform": usercreationform}
    return render(request, "registration.html", context)


class Customer_list(ListView):
    model = Customer
    context_object_name = "customers"
    template_name = "base/view_customers.html"


def add_custom(request):
    form = Customerform()
    if request.method == "POST":
        form = Customerform(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "customer was added succesfully")
            return redirect("view-cust")
        else:
            messages.error(request, "error occured")
    context = {"form": form}
    return render(request, "base/add_customers.html", context)


class Customer_detail(DetailView):
    model = Customer
    context_object_name = "customer"
    template_name = "base/view_customers.html"


class Customer_update(UpdateView):
    model = Customer
    fields = "__all__"
    success_url = reverse_lazy("view-cust")
    template_name = "base/add_customers.html"
