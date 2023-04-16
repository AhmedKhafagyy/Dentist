from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),
    path('price.html', views.price, name='price'),
    path('service.html', views.service, name='service'),
    path('appointment.html', views.appointment, name='appointment'),
]
