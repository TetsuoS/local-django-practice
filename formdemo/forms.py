from django import forms
from .models import Formdemo

class FormdemoCreateForm(forms.ModelForm):

    class Meta:
        model = Formdemo
        fields = '__all__'
