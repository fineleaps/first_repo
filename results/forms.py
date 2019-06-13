from django import forms
from .models import Result


class ResultAddForm(forms.Form):

    class Meta:
        fields = ('result_choice', "details")
