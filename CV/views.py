from django.shortcuts import render
from .models import CustomUser, ProfecionalSkills

# Create your views here.

def CV_view(request):
    
    user = CustomUser.objects.all()[0]
    profecional_skills = ProfecionalSkills.objects.filter(user=user).order_by("-experiance_lvl")
    context = {
        "user":user,
        "profecional_skills": profecional_skills,

        }

    return render(request, "CV/index.html",context)