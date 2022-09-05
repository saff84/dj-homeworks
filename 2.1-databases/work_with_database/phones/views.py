from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):

    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get("sort",)
    phones_object = Phone.objects.all()
    print(sort)
    phones = [

        {'name': p.name,
         'price': p.price,
         'image': p.image,
         'release_date': p.release_date,
         'lte_exists': p.lte_exists,
         'slug': p.slug}
        for p in phones_object]

    context = {'phones': phones}

    if sort == 'name':
        name = sorted(phones, key=lambda p: p['name'])

        context = {'phones': name}

    elif sort == 'min_price':
        min_price = sorted(phones, key=lambda p: p['price'])

        context = {'phones': min_price}

    elif sort == 'max_price':
        max_price = sorted(phones, key=lambda p: p['price'], reverse=True)

        context = {'phones': max_price}

    # context = {'phones': phones}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones_object = Phone.objects.all()
    for p in phones_object:
        if p.slug == slug:
            phone = {
                'name': p.name,
                'price': p.price,
                'image': p.image,
                'release_date': p.release_date,
                'lte_exists': p.lte_exists,
                'slug': p.slug}

    context = {'phone': phone}

    return render(request, template, context)
