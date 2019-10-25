from django import forms
from app.models import otp
class otp_form(forms.ModelForm):
    class Meta:
        model=otp
        fields='__all__'