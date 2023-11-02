from django.shortcuts import render
from .models import CustomUser, ProfecionalSkills, WorkExperiance, Education, Projects, SocialMedia
from django.http import HttpRequest, JsonResponse
from .forms import ContactUsDataForm
from .async_email import send_mail
import time
from threading import Thread
# send mail ----------------------------------------------------------------------------------------

from django.template.loader import render_to_string

# --------------------------------------------------------------------------------------------------
# Create your views here.




async def CV_view(request: HttpRequest):
    
    # querys are here -----------------------------------------------------------------------------
    user = CustomUser.objects.all()[0]
    profecional_skills = ProfecionalSkills.objects.filter(user=user).order_by("-experiance_lvl")
    work_experiances = WorkExperiance.objects.filter(user=user).order_by("-start_date")
    educations = Education.objects.filter(user=user).order_by("start_date")
    projects = Projects.objects.filter(user=user)
    socials = SocialMedia.objects.all()

    # ---------------------------------------------------------------------------------------------
    # form render ---------------------------------------------------------------------------------
    form = ContactUsDataForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()


            # send email for admin -----------------------------------------------------------------
            email_content_for_admin = render_to_string("emails/contact_us_form/admin.html", context={
                "name": request.POST.get("name"),
                "email": request.POST.get("email"),
                "message": request.POST.get("message")
            })

            thread_admin = Thread(target=send_mail,
                                args=("contact form submitation",
                                    email_content_for_admin,
                                    "a.a.s.javid0416@gmail.com",
                                    ["a.a.s.javid0416.gaming@gmail.com"])
                                )
            
            thread_admin.start()
            # end -----------------------------------------------------------------------------------
            # send email for client -----------------------------------------------------------------

            email_content_for_client = render_to_string("emails/contact_us_form/client.html", context={
                "name": request.POST.get("name"),
            })

            client_thread = Thread(target=send_mail,
                                args=("contact form submitation",
                                    email_content_for_client,
                                    "a.a.s.javid0416@gmail.com",
                                    [request.POST.get("email")])
                                )
            
            client_thread.start()
            # end ------------------------------------------------------------------------------------

            return JsonResponse({'message': 'Data saved successfully!'})
        else:
            form = ContactUsDataForm()
            errors = form.errors
            return JsonResponse({'errors': errors}, status=400)

    # ----------------------------------------------------------------------------------------------

    # send mail ------------------------------------------------------------------------------------


    # ----------------------------------------------------------------------------------------------
    # context data here ----------------------------------------------------------------------------
    
    context = {
        "user":user,
        "profecional_skills": profecional_skills,
        "work_experiances": work_experiances,
        "educations": educations,
        "projects":projects,
        "form": form,
        "socials": socials,
        }
    # -----------------------------------------------------------------------------------------------
    return render(request, "CV/index.html",context)