from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import logout
from controlpanel.forms import LoginForm
import ipdb


@login_required(login_url="/login")
def restricted_page_view(request):
    TEMPLATE_URL = "restricted_page.html"
    request_dictionary = RequestContext(request)
    request_dictionary["user_email"] = request.user.email
    return render(request, TEMPLATE_URL, {"user_email": request.user.email})


def login_page_view(request):
    TEMPLATE_URL = "login.html"
    if request.method == "POST":
        login_form = LoginForm(request, request.POST)
        if login_form.is_valid():
            return redirect("/")
    return render(request, TEMPLATE_URL)


def logout_page_view(request):
    logout(request)
    return redirect("/login")
