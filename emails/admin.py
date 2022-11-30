from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(NewsletterEmails)

admin.site.register(ContactData)

admin.site.register(SentedEmails)

