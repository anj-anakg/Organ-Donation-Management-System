from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView

from .models import Donar


# Create your views here.
def home(request):
    return render(request, 'home.html')


def main(request):
    return render(request, 'main.html')


def faq(request):
    return render(request, 'faq.html')


def contact(request):
    return render(request, 'contact.html')


def donar_details(request):
    return render(request, 'donor_details.html')


def about(request):
    return render(request, 'about.html')


def approved_hospitals(request):
    return render(request, 'Approved_hospitals.html')


class SearchResultView(LoginRequiredMixin, ListView):
    model = Donar
    template_name = 'donor_details.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Donar.objects.filter(
            Q(bloodgroup=query) | Q(organ=query)
        )


class AddDonor(CreateView):
    model = Donar
    fields = '__all__'
    success_url = reverse_lazy('donor_card_details')

    template_name = 'donor_card.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddDonor, self).form_valid(form)


class DonorList(LoginRequiredMixin, ListView):
    model = Donar
    context_object_name = 'donor_list'
    template_name = 'donor_card_details.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class DonorUpdate(LoginRequiredMixin, UpdateView):
    model = Donar
    fields = '__all__'
    success_url = reverse_lazy('donor_card_details')
    template_name = 'donor_card_update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


