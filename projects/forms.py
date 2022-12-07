from django import forms
from . import models
from django.utils.translation import gettext as _


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Projects
        fields = [_('title'), _('short_description'), _('image')]


