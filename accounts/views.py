from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render


def login_view(request):
    form = AuthenticationForm(request=request)

    return render(
        request,
        "accounts/login.html",
        {"form": form}
        )
