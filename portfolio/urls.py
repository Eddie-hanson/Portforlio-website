from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("experience/", views.experience, name="experience"),
    path("certification/", views.certification, name="certification"),
    path("contact/", views.contact, name="contact"),
    path("projects/", views.projects, name="projects"),
    path("resume/", views.resume, name="resume"),
]
