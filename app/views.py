from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string


# Create your views here.
def home(request):


    return render(request, 'index.html')