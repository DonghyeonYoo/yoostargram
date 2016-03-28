from django.views.generic import View
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib import messages


class SignupView(View):

    def get(self, request):
        return render(
            request,
            "users/signup.html",
            context={},
        )

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        description = request.POST.get("description")

        user = get_user_model().objects.create_user(
            username=username,
            password=password,
            description=description,
        )
        return redirect(reverse("home"))
