from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def About(request):
    return render(request, "about.html")


def certification(request):
    return render(request, "certification.html")


def contact(request):
    return render(request, "contact.html")


def projects(request):
    project_show = [
        {'title': 'University Of Ghana Computer Science Webpage Mockup',
         'image': 'assests/UG.png'},
        {'title': 'Snake Game with python and......',
         'image': 'assests/snake.png'},
        {'title': 'Ecommerce website',
         'image': 'assests/ecom.png'},
        {'title': 'Rest API ',
         'image': 'assests/REST.png'},
        {'title': 'ISS TRACKER',
         'image': 'assests/iss.png'},
    ]
    return render(request, "projects.html", {"projects": project_show})
