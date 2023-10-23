from django import forms
from . import models


class TechnologiesAdminForm(forms.ModelForm):
    class Meta:
        model = models.Technologies
        fields = "__all__"
    def clean(self):
        cleaned_data = super().clean()

        field_value = self.cleaned_data.get("name")
        if_exist_value = models.Technologies.objects.filter(name__iexact=field_value).first()
        if if_exist_value:
            self.add_error("name", f"the {if_exist_value} alredy exist")
        
        return cleaned_data

