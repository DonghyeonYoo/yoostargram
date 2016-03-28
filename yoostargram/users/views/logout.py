from django.contrib.auth import logout
from django.views.generic import View
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib import messages


class LogoutView(View):

    def get(self, request):
        logout(request)
        messages.add_message(
            request,
            messages.SUCCESS,
            "logout is SUCCESSED",
        )
        return redirect(reverse("home"))
