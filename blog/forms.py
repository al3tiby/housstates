from django import forms
from . import models
from django.utils.translation import gettext as _


class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = [_('title'), _('short_description'), _('description'), _('image')]


