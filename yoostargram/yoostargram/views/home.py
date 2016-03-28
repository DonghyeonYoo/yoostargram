from django.shortcuts import render


def home(models.Model):
    context = {
    }

    return render(
        request,
        "home.html",
        context,
    )
