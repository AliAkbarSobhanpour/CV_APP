from django.urls import path
from .views import CV_view


urlpatterns = [
    path("", CV_view, name="CV-view")
]



