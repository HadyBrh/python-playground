from django import forms
from vacation_aiia.models import Vacation

class VacationForm(forms.ModelForm):
    class Meta:
        model = Vacation
        fields = "__all__"
