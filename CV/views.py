from django.shortcuts import render
from .models import CustomUser, ProfecionalSkills, WorkExperiance, Education, Projects

# Create your views here.

def CV_view(request):
    
    user = CustomUser.objects.all()[0]
    profecional_skills = ProfecionalSkills.objects.filter(user=user).order_by("-experiance_lvl")
    work_experiances = WorkExperiance.objects.filter(user=user).order_by("-start_date")
    educations = Education.objects.filter(user=user).order_by("start_date")
    projects = Projects.objects.filter(user=user)
    context = {
        "user":user,
        "profecional_skills": profecional_skills,
        "work_experiances": work_experiances,
        "educations": educations,
        "projects":projects
        }

    return render(request, "CV/index.html",context)