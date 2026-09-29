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
        
    form = form if request.method == "POST" else AssistanceRequestForm()

    error_step = 1

    error_steps = {
        "vehicle_registration": 1,
        "vehicle_type": 1,
        "vehicle_make": 1,
        "vehicle_model": 1,
        "vehicle_description": 1,
        "problem_type": 2,
        "problem_description": 2,
        "location_type": 3,
        "location_postcode": 3,
        "location_description": 3,
        "location_direction": 3,
        "location_access": 3,
        "occupant_count": 4,
        "assistance_needs": 4,
        "assistance_details": 4,
        "occupant_safety": 4,
        "contact_first_name": 5,
        "contact_last_name": 5,
        "contact_phone": 5,
        "contact_email": 5,
        "contact_notes": 5,
    }

    if form.errors:
        error_step = min(
            error_steps.get(field_name, 1)
            for field_name in form.errors
        )

    return render(
        request,
        "assistance.html",
       {
            "form": form,
            "error_step": error_step,
       },
    )
        
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
