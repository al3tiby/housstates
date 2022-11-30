from django.db import models

# Create your models here.

class NewsletterEmails(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()

    def __str__(self):
        return self.customer_name


class ContactData(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_message = models.TextField(max_length=500)

    def __str__(self):
        return self.customer_name


class SentedEmails(models.Model):
    email_subject = models.CharField(max_length=250)
    email_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.email_subject