from django.shortcuts import render

from .forms import AssistanceRequestForm


def request_assistance(request):
    if request.method == "POST":
        form = AssistanceRequestForm(request.POST)

        if form.is_valid():
            assistance_request = form.save()

            return render(
                request,
                "assistance-confirmation.html",
                {"assistance_request": assistance_request},
            )

    return render(request, "assistance.html")