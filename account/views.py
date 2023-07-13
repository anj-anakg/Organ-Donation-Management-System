from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('main')
    redirect_authenticated_user = True
    template_name = 'registration.html'


