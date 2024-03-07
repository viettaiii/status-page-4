from django import forms
from .models import Function


class FunctionForm(forms.ModelForm):
    class Meta:
        model = Function
        fields = ('title', 'publication_date', 'function_type', )
