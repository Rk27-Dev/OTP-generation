from django import forms
from app.models import otpmodel
class otp_form(forms.ModelForm):
    class Meta:
        model=otpmodel
        fields='__all__'