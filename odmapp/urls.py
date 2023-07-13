from django.urls import path

from . import views
from .views import SearchResultView, AddDonor, DonorList, DonorUpdate

urlpatterns = [
    path('home/', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('approved_hospitals/', views.approved_hospitals, name='approved_hospitals'),
    path('about/', views.about, name='about'),
    path('details/', views.donar_details, name='details'),
    path('search/', SearchResultView.as_view(), name='search_results'),
    path('donor_card/', AddDonor.as_view(), name='donor_card'),
    path('donor_list/', DonorList.as_view(), name='donor_card_details'),
    path('donor_update/<int:pk>/', DonorUpdate.as_view(), name='donor_card_update'),
]
