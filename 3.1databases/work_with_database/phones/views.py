from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    print(request.GET)
    sort = request.GET.get('sort')
    template = 'catalog.html'
    phones = Phone.objects.all()

    if sort == 'name':
        phones = sorted(phones, key=lambda phone: phone.name)
    if sort == 'min_price':
        phones = sorted(phones, key=lambda phone: phone.price)
    if sort == 'max_price':
        phones = sorted(phones, key=lambda phone: phone.price, reverse=True)

    context = {'phones': phones}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)[0]
    print(phone)
    context = {'phone': phone}
    return render(request, template, context)
