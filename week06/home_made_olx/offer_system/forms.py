from django import forms

from .models import Offer

class CreateOfferModelForm(forms.ModelForm):

    class Meta:
        model = Offer
        fields = ('title', 'category', 'price', 'description', 'image', 'author')
