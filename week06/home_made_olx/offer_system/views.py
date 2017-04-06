from django.shortcuts import render

from .models import Offer

from .forms import CreateOfferModelForm
# Create your views here.

def index_view(request):
    offers = Offer.objects.prefetch_related('category').select_related('author').all()
    return render(request, 'index.html', locals())


def create_offer_view(request):
    form = CreateOfferModelForm()
    if request.method == 'POST':
        form = CreateOfferModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

    return render(request, 'create_offer.html', locals())


def get_stats_view(request):
    top_categories = [1, 2, 3, 4]
    top_users = [1 ,2, 3, 4]
    return render(request, 'stats.html', locals())
