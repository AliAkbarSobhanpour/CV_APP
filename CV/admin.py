from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.CustomUser)
admin.site.register(models.SocialMedia)
admin.site.register(models.WorkExperiance)
admin.site.register(models.Education)
admin.site.register(models.Technologies)
admin.site.register(models.Projects)
admin.site.register(models.ProfecionalSkills)