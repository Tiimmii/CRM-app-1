from django import forms
from . models import Lead

class LeadCreateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "first_name",
            "last_name",
            "age",
            "agent",
            "image",
        )