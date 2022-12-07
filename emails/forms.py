from django import forms
from tinymce.widgets import TinyMCE
from django.utils.translation import gettext as _


class NewsletterForm(forms.Form):
    subject = forms.CharField(label=_("Subject"))
    message = forms.CharField(widget=TinyMCE(), label=_("Email content"))

