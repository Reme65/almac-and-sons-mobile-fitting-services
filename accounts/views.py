from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(
            request=request,
            data=request.POST,
        )

        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
    else:
        form = AuthenticationForm(request=request)

    return render(
        request,
        "accounts/login.html",
        {"form": form},
    )
def logout_view(request):
    logout(request)
    return redirect("home")

