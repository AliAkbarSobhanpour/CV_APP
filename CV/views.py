from django.shortcuts import render

# Create your views here.

def CV_view(request):
    

    context = {}

    return render(request, "CV/index.html",context)