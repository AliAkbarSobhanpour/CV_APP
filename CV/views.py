from django.shortcuts import render
from .models import CustomUser

# Create your views here.

def CV_view(request):
    
    user = CustomUser.objects.all()[0]

    context = {"user":user}

    return render(request, "CV/index.html",context)