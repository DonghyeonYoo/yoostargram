from django.views.generic import View
from django.shortcuts import render


class SignupView(View):

    def get(self, request):
        return render(
            request,
            "users/signup.html",
            context={},
        )

    def post(self, request):
        pass
