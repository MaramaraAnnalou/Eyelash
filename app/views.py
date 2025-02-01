from audioop import reverse
from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.contrib.auth.models import User

from .models import UserProfile
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = 'app/Home.html'

class AboutPageView(TemplateView):
        template_name = 'app/About.html'

class AppointmentListView(ListView):
    model = UserProfile
    context_object_name = 'appointment_list'
    template_name = 'app/AppointmentList.html'

class AppointmentDetailView(DetailView):
    model = UserProfile
    context_object_name = 'appointment'
    template_name = 'app/AppointmentDetail.html'

class AppointmentCreateView(CreateView):
    model = UserProfile
    fields = ['user', 'phone_number', 'address' , 'profile_picture']
    template_name = 'app/AppointmentCreate.html'




class AppointmentUpdateView(UpdateView):
    model = UserProfile
    fields = ['user', 'phone_number', 'address' , 'profile_picture']
    template_name = 'app/AppointmentUpdate.html'

class AppointmentDeleteView(DeleteView):
    model = UserProfile
    template_name = 'app/AppointmentDelete.html'
    success_url = reverse_lazy('AppointmentList')