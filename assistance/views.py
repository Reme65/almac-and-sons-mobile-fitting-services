from django.shortcuts import render

from .forms import AssistanceRequestForm


def request_assistance(request):
    if request.method == "POST":
        form = AssistanceRequestForm(request.POST)

        if form.is_valid():
            form.save()

    return render(request, "assistance.html")
