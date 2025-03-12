from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string


# Create your views here.
def home(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")

        email_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{subject}"

        try:
            send_mail(
                subject="New Message",
                message=email_body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False
            )
            messages.success(request, "Your message was successfully sent")
        except Exception as e:
            messages.error(request, f"Failed to send message. Error: {str(e)}")

        return redirect("home")


    return render(request, 'index.html')