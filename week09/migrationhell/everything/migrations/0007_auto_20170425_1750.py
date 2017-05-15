# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 17:50
from __future__ import unicode_literals

from django.db import migrations


def copy_products(apps, schema_editor):
    OldProducts = apps.get_model('everything', 'Product')
    NewProducts = apps.get_model('products', 'Product')

    for old_p in OldProducts.objects.all():
        real_product = NewProducts.objects.create(uuid=old_p.uuid,
                                                  name=old_p.name,
                                                  categories=old_p.categories)

        for c in old_p.comments.all():
            real_product.comments.add(c)


def copy_category(apps, schema_editor):
    OldCat = apps.get_model('everything', 'Category')
    NewCat = apps.get_model('products', 'Category')

    for old_c in OldCat.objects.all():
        NewCat.objects.create(id=old.id,
                              name=old.name)


def copy_invoice(apps, schema_editor):
    OldInvoice = apps.get_model('everything', 'Invoice')
    NewInvoice = apps.get_model('cart', 'Invoice')

    for old_i in OldInvoice.objects.all():
        NewInvoice.objects.create(id=old_i.id,
                                  company_data=old_i.company_data,
                                  order=old_i.order)


def copy_order(apps, schema_editor):
    OldOrder = apps.get_model('everything', 'Order')
    NewOrder = apps.get_model('cart', 'Order')

    for old in OldOrder.objects.all():
        real_order = NewOrder.objects.create(uuid=old.uuid,
                                             user=old.user)

        for p in old.products:
            real_order.products.add(p)


def copy_comments(apps, schema_editor):
    OldComments = apps.get_model('everything', 'Comment')
    NewComments = apps.get_model('comments', 'Comment')

    for old in OldComments.objects.all():
        NewComments.objects.create(id=old.id,
                                   text=old.text,
                                   user=old.user,
                                   product=old.product)


def call_data_migrations(*args, **kwargs):
    copy_products(*args, **kwargs)
    copy_category(*args, **kwargs)
    copy_invoice(*args, **kwargs)
    copy_comments(*args, **kwargs)


class Migration(migrations.Migration):

    dependencies = [
        ('everything', '0006_merge_20170425_1728'),
    ]

    operations = [
            migrations.RunPython(call_data_migrations)
    ]