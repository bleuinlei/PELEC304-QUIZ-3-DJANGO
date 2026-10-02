from django.shortcuts import render
from .models import Student

def home(request):
    students = Student.objects.all().order_by('-created_at')
    return render(request, 'main/home.html', {'students': students})
