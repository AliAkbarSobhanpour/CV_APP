from django.contrib import admin
from . import models
from .forms import TechnologiesAdminForm
# Register your models here.

class TechnologiesModelAdmin(admin.ModelAdmin):
    form = TechnologiesAdminForm

admin.site.register(models.CustomUser)
admin.site.register(models.SocialMedia)
admin.site.register(models.WorkExperiance)
admin.site.register(models.Education)
admin.site.register(models.Technologies, TechnologiesModelAdmin)
admin.site.register(models.Projects)
admin.site.register(models.ProfecionalSkills)
admin.site.register(models.ContactUsData)
admin.site.register(models.Book)