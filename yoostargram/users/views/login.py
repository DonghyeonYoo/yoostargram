from django.contrib.auth import login, authenticate
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages


class LoginView(View):

    def get(self, request):
        template_name = "users/login.html"

        return render(
            request,
            template_name,
            context={},
        )

    def post(self, request):
        my_username = request.POST.get('my_username')
        my_password = request.POST.get('my_password')

        user = authenticate(
                username=my_username,
                password=my_password,
        )

        if user:
            login(request, user)
            messages.add_message(
                request,
                messages.SUCCESS,
                "login is successed",
            )
            return redirect(reverse('home'))
        return redirect(reverse('login'))
