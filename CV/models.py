from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator
# Create your models here.

class CustomUser(AbstractUser):
    address = RichTextField("address")
    position_name = models.CharField("position name", max_length=200, help_text="maximum 25 char")
    image = models.ImageField("avatar", upload_to="avatars/")
    age = models.IntegerField(blank=True,null=True)
    about = RichTextField("about your self")
    phone_number = PhoneNumberField("phone number", region="IR", blank=True)
    

class SocialMedia(models.Model):
    app = models.CharField("app name", max_length=50)
    url = models.URLField("app adress",max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "social media"
        verbose_name_plural = "social medias"


class WorkExperiance(models.Model):
    position = models.CharField("workin position", max_length=200)
    at = models.CharField("company", max_length=200)
    at_url = models.URLField("company address", max_length=200)
    start_date = models.DateTimeField("start date")
    end_date = models.DateTimeField("end date", blank=True, null=True)
    until_present = models.BooleanField()
    about = RichTextField("about job", help_text="how it was? \n what do you do there \n and ...")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "work experiance"
        verbose_name_plural = "work experiances"

class Education(models.Model):
    learned_skill = models.CharField("learned skill", max_length=200)
    from_where = models.CharField("univercity or instutute", max_length=200)
    from_where_url = models.URLField("univercity of instutute url", max_length=200)
    start_date = models.DateTimeField("start date")
    end_date = models.DateTimeField("end date", blank=True, null=True)
    until_present = models.BooleanField()
    about = RichTextField("about education")
    certificate = models.URLField("certificate url")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "education"
        verbose_name_plural = "educations"

class Technologies(models.Model):
    name = models.CharField("technology title",max_length=200)

    class Meta:
        verbose_name = "technology"
        verbose_name_plural = "tecmologies"

    def __str__(self):
        return self.name

class Projects(models.Model):
    project_name = models.CharField("project name", max_length=200)
    for_where = models.CharField( "for where", max_length=50, help_text="if is a open surce in github pls github \n if is for a company pls load image for that from link bellow")
    company_logo = models.ImageField("logo of company",upload_to="logos/",help_text="if project is for a company pls setcompany logo")
    about = RichTextField("about projects")
    technologies = models.ManyToManyField(Technologies)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"
    


class ProfecionalSkills(models.Model):
    technologies = models.ForeignKey(Technologies, on_delete=models.CASCADE)
    experiance_lvl = models.IntegerField("experiance level",
                                        help_text="this is based on how many year that you are working - max value 5",
                                        validators=[MaxValueValidator(5)])
    user= models.ForeignKey(CustomUser, models.CASCADE)
    class Meta:
        verbose_name = "profecional skill"
        verbose_name_plural = "profecional skills"

    def __str__(self):
        return self.technologies.name
    

