from django.shortcuts import render


def request_assistance(request):
    return render(request, "assistance.html")
