from django.shortcuts import render
from .models import *

# Create your views here.

def contact_form(request):
    form = contact.objects.all()
    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        phone = request.POST['phone-number']
        message = request.POST['message']
        contact_info = contact(first_name=first_name, last_name=last_name, email=email, phone_number=phone, message=message)
        contact_info.save()
    else:
        print('Not sent')
    return render(request, 'index.html', {'form': form})