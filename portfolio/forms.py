from django import forms
from .models import Project,BannerImage

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'date', 'category', 'description', 'thumbnail', 'locations']

    # Define widgets and form field options here


class BannerImageForm(forms.ModelForm):
    class Meta:
        model = BannerImage
        fields = ['image']
