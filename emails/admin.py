from django.contrib import admin

# Register your models here.

from . import models


@admin.register(models.NewsletterEmails)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'customer_email', 'created_at']
    list_per_page = 30

    def id(self, obj):
        return obj

    def customer_name(self, obj):
        return obj

    def customer_email(self, obj):
        return obj

    def created_at(self, obj):
        return obj


admin.site.register(models.SentedEmails)



@admin.register(models.ContactData)
class ContactDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'customer_email', 'created_at']
    list_per_page = 30

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def id(self, obj):
        return obj

    def customer_name(self, obj):
        return obj

    def customer_email(self, obj):
        return obj

    def created_at(self, obj):
        return obj

