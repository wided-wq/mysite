from django.shortcuts import render
from .models import Courses
# Create your views here.


def first_view(request):
    data= Courses.objects.all()
    print(data)
    return render(request=request,template_name="test.html")
