from django import forms
from . import models
from django.utils.translation import gettext as _


class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ['title', 'short_description', 'description', 'image']


