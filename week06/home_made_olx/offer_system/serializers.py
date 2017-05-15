from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from moneyed import Money

from .models import Offer, Category


class MoneyField(serializers.Field):
    def to_representation(self, obj):
        return {
            'amount': "%f" % (obj.amount),
            'currency': "%s" % (obj.currency),
        }
    def to_internal_value(self, data):
        return Money(data['amount'], data['currency'])


class OfferSerializer(ModelSerializer):
    price = MoneyField()
    class Meta:
        model = Offer
        fields = ('title',
                  'description',
                  'price',
                  'created_at',
                  'author')
