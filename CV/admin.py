
from django.contrib import admin
from . import models
from django import forms
# Register your models here.

class TechnologiesAdminForm(forms.ModelForm):
    class Meta:
        model = models.Technologies
        fields = "__all__"
    def clean(self):
        cleaned_data = super().clean()

        field_value = self.cleaned_data.get("name")
        print(field_value)
        value_pair = models.Technologies.objects.filter(name__iexact=field_value).first()
        if value_pair:
            self.add_error("name", f"the {value_pair} alredy exist")
        
        return cleaned_data
    
class TechnologiesModelAdmin(admin.ModelAdmin):
    form = TechnologiesAdminForm

admin.site.register(models.CustomUser)
admin.site.register(models.SocialMedia)
admin.site.register(models.WorkExperiance)
admin.site.register(models.Education)
admin.site.register(models.Technologies, TechnologiesModelAdmin)
admin.site.register(models.Projects)
admin.site.register(models.ProfecionalSkills)