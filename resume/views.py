from django.shortcuts import render, redirect
from .models import Contact
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
        contact = Contact()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_address = request.POST.get('email_address')
        message = request.POST.get('message')
        contact.first_name = first_name
        contact.last_name = last_name
        contact.email_address = email_address
        contact.message = message
        contact.save()
        return HttpResponse("<h1>Success! Thank you for your message.</h1>")
    return render(request, 'resume/resume_view.html', {})