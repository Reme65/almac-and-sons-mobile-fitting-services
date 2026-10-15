from django.contrib.auth.decorators import login_required
from assistance.models import AssistanceRequest
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST


@require_POST
def logout_view(request):
    logout(request)
    return redirect("home")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(
            request=request,
            data=request.POST,
        )

        if form.is_valid():
            login(request, form.get_user())

            next_url = request.POST.get("next") or request.GET.get("next")

            if next_url and url_has_allowed_host_and_scheme(
                url=next_url,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure(),
            ):
                return redirect(next_url)

            return redirect("home")

    else:
        form = AuthenticationForm(request=request)

    return render(
        request,
        "accounts/login.html",
        {"form": form},
    )

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )

@login_required
def dashboard_view(request):
    assistance_requests = AssistanceRequest.objects.filter(
        customer=request.user
    ).order_by("-created_at")

    return render(
        request,
        "accounts/dashboard.html",
        {"assistance_requests": assistance_requests},
    )
