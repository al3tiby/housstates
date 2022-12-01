from django.shortcuts import render, redirect
from django.conf import settings
from .models import *
from django.core.mail import send_mail

# Create your views here.

def contact_us(request):
    if request.method == 'POST':
        customer_name = request.POST['name']
        customer_email = request.POST['email']
        customer_message = request.POST['message']

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
