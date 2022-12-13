from django.shortcuts import render, redirect, resolve_url
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import *
from .forms import NewsletterForm
from .models import NewsletterEmails
from django.core.mail import send_mail, EmailMessage, send_mass_mail, get_connection
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.utils.translation import gettext as _



# Create your views here.

def contact_us(request):
    if request.method == 'POST':
        customer_name = request.POST['name']
        customer_email = request.POST['email']
        customer_message = request.POST['message']

        if not customer_name or not customer_email or not customer_message:
            messages.error(request, _('Please enter the currect information'))
            not_valid_information = _('Please enter a currect information')
            return render(request, 'email/contact/contact_us.html', {'not_valid_information': not_valid_information})

        save_contact = ContactData.objects.create(
            customer_name=customer_name,
            customer_email=customer_email,
            customer_message=customer_message
        )
        save_contact.save()

        save_contact.id
        send_mail(
            f'Email #{save_contact.id} from {save_contact.customer_name}',
            f'From email: {save_contact.customer_email}\n\n{save_contact.customer_message}',
            save_contact.customer_email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )


        thank_you_customer = customer_name
        return render(request, 'email/contact/contact_us.html', {'thank_you_customer': thank_you_customer})

    else:
        return render(request, 'email/contact/contact_us.html', {})



def newsletteremails(request):
    if request.method == 'POST':
        newsletter_name = request.POST.get('name', None)
        newsletter_email = request.POST.get('email', None)

        if not newsletter_name or not newsletter_email:
            messages.error(request, _('Please enter the currect name and email address'))
            return redirect('projects')

        if NewsletterEmails.objects.filter(customer_email=newsletter_email).exists():
            messages.error(request, _(f'The email "{newsletter_email}" already registered'))
            return redirect('projects')

        try:
            validate_email(newsletter_email)
        except ValidationError as e:
            messages.error(request, e.message[0])
            return redirect('projects')


        save_newsletter_user = NewsletterEmails.objects.create(
            customer_name=newsletter_name,
            customer_email=newsletter_email
        )
        save_newsletter_user.save()
        messages.success(request, _(f'{newsletter_email} email was successfully subscribed to our newsletter!'))
        return redirect('projects')

    else:
        return redirect('projects')

    return render(request, 'email/newsletter.html', {})



@user_passes_test((lambda u: u.is_superuser), 'admin_login')
def newsletter_senders(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            emails = ','.join([active.customer_email for active in NewsletterEmails.objects.all()]).split(',')

            mail = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                bcc=emails
            )
            mail.content_subtype = 'html'

            if mail.send():
                messages.success(request, _("Email sent successfully"))
                save_sented_newsletter = SentedEmails.objects.create(
                    email_subject=subject,
                    email_body=message
                )
                save_sented_newsletter.save()

            else:
                messages.error(request, _("There was an error sending email"))

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('control_panel')


    form = NewsletterForm()
    context = {
        'form': form
    }
    return render(request, 'email/send/send_email.html', context)