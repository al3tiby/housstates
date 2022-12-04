from django import forms
from . import models
from django.utils.translation import gettext as _


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Projects
        fields = ['title', 'short_description', 'image']


