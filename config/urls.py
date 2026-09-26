from django.contrib import admin
from django.urls import path

from core import views as core_views
from assistance import views as assistance_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", core_views.home, name="home"),
    path("services/", core_views.services, name="services"),
    path(
        "assistance/",
        assistance_views.request_assistance,
        name="request_assistance",
    ),
]
