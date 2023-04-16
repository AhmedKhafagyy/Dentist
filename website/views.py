from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message = request.POST['message']

        # send an email
        send_mail(
            message_subject,
            message,
            message_email,  # from email
            ['a4a0c5f730@fireboxmail.lol'],  # to email
        )

        return render(request, 'contact.html', {'name': name})
    else:
        return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def price(request):
    return render(request, 'price.html')


def service(request):
    return render(request, 'service.html')


def appointment(request):
    if request.method == "POST":
        your_name = request.POST['app_name']
        your_email = request.POST['app_email']
        your_date = request.POST['app_date']
        your_time = request.POST['app_time']
        your_service = request.POST['app_service']
        your_doctor = request.POST['app_doctor']

        appointment_message = "Name: "+your_name+" Date: "+str(your_date)+" Time: "+str(
            your_time)+" Service: " + str(your_service)+" Doctor: "+str(your_doctor)

        send_mail(
            'Appointment Request',
            appointment_message,
            your_email,  # from email
            ['a4a0c5f730@fireboxmail.lol'],  # to email
        )

        return render(request, 'review.html', {
            'your_name': your_name,
            'your_email': your_email,
            'your_date': your_date,
            'your_time': your_time,
            'your_service': your_service,
            'your_doctor': your_doctor
        })
    else:
        return render(request, 'appointment.html')


'''
    appointment_message = "Name: "+str(your_name)+" Date: "+str(your_date)+" Time: "+str(your_time)+" Service: " +
    str(your_service)+" Doctor: "+str(your_doctor)

        send_mail(
            'Appointment Request',
            appointment_message,
            your_email,  # from email
            ['a4a0c5f730@fireboxmail.lol'],  # to email
        )
'''
