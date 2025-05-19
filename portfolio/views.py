from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def experience(request):
    return render(request, "experience.html")


def certification(request):
    certifications = [{
        'title': 'Certificate in Computer Networking',
        'Source': 'Shiv-India Institute of Management and Technology'
    },
        {
        'title': 'Building Web Applications with Django and Postgres',
        'Source': 'Udemy'
    },
        {
        'title': 'Django Rest Framework For Absolute Beginners',
        'Source': 'Udemy'
    },
        {
        'title': 'Computer Vision Fundamentals',
        'Source': 'Udemy'
    }]
    return render(request, "certification.html", {'certifications': certifications})


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
