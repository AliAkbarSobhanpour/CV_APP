from django.shortcuts import render
from .models import CustomUser, ProfecionalSkills, WorkExperiance, Education, Projects
from django.http import HttpRequest, JsonResponse
from .forms import ContactUsDataForm
from django.shortcuts import redirect
# Create your views here.

def CV_view(request: HttpRequest):
    
    # querys are here 
    user = CustomUser.objects.all()[0]
    profecional_skills = ProfecionalSkills.objects.filter(user=user).order_by("-experiance_lvl")
    work_experiances = WorkExperiance.objects.filter(user=user).order_by("-start_date")
    educations = Education.objects.filter(user=user).order_by("start_date")
    projects = Projects.objects.filter(user=user)

    # form render
    form = ContactUsDataForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Data saved successfully!'})
        else:
            form = ContactUsDataForm()
            errors = form.errors
            return JsonResponse({'errors': errors}, status=400)



    context = {
        "user":user,
        "profecional_skills": profecional_skills,
        "work_experiances": work_experiances,
        "educations": educations,
        "projects":projects,
        "form": form
        }

    return render(request, "CV/index.html",context)