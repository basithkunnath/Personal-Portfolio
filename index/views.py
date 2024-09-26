from django.shortcuts import render
from .models import About
from .models import Services
from .models import Projects
from .models import Contact
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    about_info = About.objects.first()  # Assuming you'll have one "About" entry
    services_info = Services.objects.first()  # Assuming you'll have one "Services" entry
    projects_info = Projects.objects.all()  # Retrieve all project entries
    contact_info = Contact.objects.first()
    context={'about_info': about_info,
             'services_info': services_info,
             'projects_info': projects_info,
             'contact_info': contact_info
             }
    
    # CONTACT FORM
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        form_data = {
            'name':name,
            'phone':phone,
            'message':message,
        }
        message = '''
        From:\n\t\t{}\n
        Message:\n\t\t{}\n
        Phone:\n\t\t{}\n
        '''.format(form_data['name'], form_data['message'],form_data['phone'])
        send_mail('You got a mail!', message, '', ['basith6k@gmail.com']) # TODO: enter your email address
    
    return render(request,'index.html',context,)