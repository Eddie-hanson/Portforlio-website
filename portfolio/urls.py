from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("About/", views.About, name="About"),
    path("certification/", views.certification, name="certification"),
    path("contact/", views.contact, name="contact"),
    path("projects/", views.projects, name="projects"),
]
