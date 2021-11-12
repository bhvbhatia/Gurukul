from django.shortcuts import render

# Create your views her

def home(request):
    return render(request,'Tution_app/home.html')

def about(request):
    return render(request,'Tution_app/about.html')

def tutor(request):
    return render(request,'Tution_app/tutor.html')

def student(request):
    return render(request,'Tution_app/student.html')

def contact(request):
    return render(request,'Tution_app/contact.html')
