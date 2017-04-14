from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import get_user

from .models import Offer
from .queries import OfferQuerySet
from .forms import CreateOfferModelForm, PendingOfferModelForm
from .mixins import CanUpdateOfferMixin, IsSuperUserMixin

from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView

from .forms import CreateOfferModelForm
# Create your views here.

class OfferListView(LoginRequiredMixin, ListView):
    queryset = Offer.objects.prefetch_related().select_related()

    login_url = reverse_lazy('author:login')


class PendingOffers(LoginRequiredMixin, IsSuperUserMixin, ListView):
    login_url= reverse_lazy('author:login')

    model = Offer
    queryset = Offer.objects.prefetch_related().select_related()

    template_name = 'offer_system/pending_offers.html'

    def get_context_data(self, **kwargs):
        context = super(PendingOffers, self).get_context_data()
        context['pending'] = Offer.stat_objects.get_pending_offer()
        return context


class MyOffersView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('author:login')

    model = Offer
    queryset = Offer.objects.prefetch_related().select_related()

    def get_context_data(self, **kwargs):
        context = super(MyOffersView, self).get_context_data()
        context['object_list'] = Offer.objects.filter(author=self.request.user).all()
        return context

class ApprovedRejectedOffers(LoginRequiredMixin, IsSuperUserMixin, ListView):
    login_url = reverse_lazy('author:login')

    model = Offer
    queryset = Offer.objects.prefetch_related().select_related()

    template_name = 'offer_system/approved_rejected_offers.html'


    def get_context_data(self, **kwargs):
        context = super(ApprovedRejectedOffers, self).get_context_data()
        context['apprrej'] = Offer.stat_objects.get_not_pending_offer()
        return context


class CreateOfferView(LoginRequiredMixin, CreateView):
    model = Offer
    login_url = reverse_lazy('author:login')
    form_class = CreateOfferModelForm

    def form_valid(self, form):
        form.instance.author = get_user(self.request)
        return super().form_valid(form)

    success_url = reverse_lazy('offer:index')


class OfferUpdate(LoginRequiredMixin, CanUpdateOfferMixin, UpdateView):
    model = Offer
    template_name_suffix = '_update_form'
    form_class = CreateOfferModelForm
    login_url = reverse_lazy('author:login')


class OfferDelete(LoginRequiredMixin, CanUpdateOfferMixin, DeleteView):
    login_url = reverse_lazy('author:login')
    model = Offer
    template_name_suffix = '_delete_form'
    success_url = reverse_lazy('offer:index')


class UpdatePendingOffer(LoginRequiredMixin, IsSuperUserMixin, UpdateView):
    model = Offer
    template_name_suffix = '_pending_update_form'
    form_class = PendingOfferModelForm
    login_url = reverse_lazy('author:login')


def create_offer_view(request):
    form = CreateOfferModelForm()
    if request.method == 'POST':
        form = CreateOfferModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

    return render(request, 'create_offer.html', locals())


class StatisticsList(LoginRequiredMixin, TemplateView):
    template_name = 'offer_system/stats.html'
    login_url = reverse_lazy('author:login')

    def get_context_data(self, **kwargs):
        context = super(StatisticsList, self).get_context_data()
        context['top_categories'] = Offer.stat_objects.get_top_categories()
        context['top_users'] = Offer.stat_objects.get_top_users()
        return context


def get_stats_view(request):
    top_categories = Offer.stat_objects.get_top_categories()
    top_users = Offer.stat_objects.get_top_users()
    return render(request, 'offer_system/stats.html', locals())
