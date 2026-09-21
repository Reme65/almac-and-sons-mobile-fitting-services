import uuid

from django.db import models


class AssistanceRequest(models.Model):
    class Status(models.TextChoices):
        AWAITING_ASSESSMENT = "awaiting_assessment", "Awaiting assessment"
        ARRANGED = "arranged", "Assistance arranged"
        IN_PROGRESS = "in_progress", "In progress"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    reference = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AWAITING_ASSESSMENT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    # Vehicle or equipment details
    vehicle_registration = models.CharField(
        max_length=20,
        blank=True,
    )
    vehicle_type = models.CharField(max_length=30)
    vehicle_make = models.CharField(
        max_length=100,
        blank=True,
    )
    vehicle_model = models.CharField(
        max_length=100,
        blank=True,
    )
    vehicle_description = models.TextField(blank=True)

    # Problem details
    problem_type = models.CharField(max_length=30)
    problem_description = models.TextField()
        # Location details
    location_type = models.CharField(max_length=30)
    location_postcode = models.CharField(
        max_length=10,
        blank=True,
    )
    location_description = models.TextField()
    location_direction = models.CharField(
        max_length=200,
        blank=True,
    )
    location_access = models.TextField(blank=True)
        # Occupants and assistance needs
    occupant_count = models.PositiveSmallIntegerField()
    assistance_needs = models.CharField(max_length=10)
    assistance_details = models.TextField(blank=True)
    occupant_safety = models.CharField(max_length=10)
        # Contact details
    contact_first_name = models.CharField(max_length=100)
    contact_last_name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=30)
    contact_email = models.EmailField(blank=True)
    contact_notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.reference} — {self.get_status_display()}"