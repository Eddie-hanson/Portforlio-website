from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.


def index(request):
    return render(request, "index.html")


def experience(request):
    experience = [{
        'Company': 'Globe ICT',
        'Role': 'Network Engineer',
        'Duration': '2 years',
    },
        {
        'Company': 'SoftNet',
        'Role': 'Software Engineer',
        'Duration': '4 Months',
    },
        {
        'Company': 'Activo',
        'Role': 'Junior Backend Engineer',
        'Duration': '6 months',
    },
        {
        'Company': 'Hive ICT',
        'Role': 'Backend Engineer (Intern)',
        'Duration': ' 15 weeks',
    },
    ]
    return render(request, "experience.html", {'experiences': experience})


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


def resume(request):
    resume_path = "myapp/resume.pdf"
    resume_path = staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, 'rb') as resume_file:
            response = HttpResponse(
                resume_file.read(), content_type="application/pdf")
            response["Content-Disposition"] = 'attachment'
            filename = 'resume'
            return response
    else:
        return HttpResponse('Resume not found')
