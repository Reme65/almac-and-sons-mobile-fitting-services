from django.shortcuts import get_object_or_404, redirect, render

from .forms import AssistanceRequestForm
from .models import AssistanceRequest

def request_assistance(request):
    if request.method == "POST":
        form = AssistanceRequestForm(request.POST)

        if form.is_valid():
            assistance_request = form.save()

            return redirect(
                "assistance_confirmation",
                reference=assistance_request.reference,
            )
        
    return render(request, "assistance.html")

def assistance_confirmation(request, reference):
    assistance_request = get_object_or_404(
        AssistanceRequest,
        reference=reference,
    )

    return render(
        request,
        "assistance-confirmation.html",
        {"assistance_request": assistance_request},
    )
