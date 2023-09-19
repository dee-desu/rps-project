from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'date', 'category', 'description', 'thumbnail', 'locations']

    # Define widgets and form field options here
