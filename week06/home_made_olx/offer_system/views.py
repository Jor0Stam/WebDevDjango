from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth import get_user

from .models import Offer
from .queries import OfferQuerySet

from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, FormView, UpdateView

from .forms import CreateOfferModelForm
# Create your views here.

class OfferListView(ListView):
    queryset = Offer.objects.prefetch_related().select_related()
    # prefetch_related = ['category']
    # select_related= ['author']
    # model = Offer


def index_view(request):
    offers = Offer.objects.prefetch_related('category').select_related('author').all()
    return render(request, 'index.html', locals())


class CreateOfferView(CreateView):
    model = Offer
    fields = ('title', 'category', 'price', 'description', 'image', 'author')

    def form_valid(self, form):
        form.instance.author = get_user(self.request)
        super().form_valid()

    def get_success_url(self):
        return reverse_lazy('offer:index')


class OfferUpdate(UpdateView):
    model = Offer
    fields = ('title', 'category', 'price', 'description', 'image', 'author')
    template_name_suffix = '_update_form'


def create_offer_view(request):
    form = CreateOfferModelForm()
    if request.method == 'POST':
        form = CreateOfferModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

    return render(request, 'create_offer.html', locals())


class StatisticsList(TemplateView):
    template_name = 'offer_system/stats.html'

    def get_context_data(self, **kwargs):
        context = super(StatisticsList, self).get_context_data()
        context['top_categories'] = Offer.stat_objects.get_top_categories()
        context['top_users'] = Offer.stat_objects.get_top_users()
        return context


def get_stats_view(request):
    top_categories = Offer.stat_objects.get_top_categories()
    top_users = Offer.stat_objects.get_top_users()
    return render(request, 'offer_system/stats.html', locals())
