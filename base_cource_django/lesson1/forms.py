from django import forms
from lesson1.models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["image", "email_user", "text", "rating", "positiv_or_negativ", "telefon_number"]
        
        widgets ={
            "rating": forms.NumberInput(attrs={"max": 10, "min": 0.0, "step": 0.1}),
            "text": forms.Textarea(attrs={"rows": 3, "placeholder": "Enter you'r report"}),
            "telefon_number": forms.TextInput(attrs={"placeholder": "+380....", "max": 13})
        } 