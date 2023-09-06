from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


def index(request):
    context = {
        'title': 'Market Place',

    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {
        'title': 'Market Place - каталог',
        'categories': ProductCategory.objects.all(),
        # 'products': Product.objects.all(),

    }
    if category_id:
        # context.update({'products': Product.objects.filter(category_id=category_id)})
        products = Product.objects.filter(category_id=category_id)
    else:
        # context.update({'products':Product.objects.all()})
        products = Product.objects.all()
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context.update({'products': page_obj})

    return render(request, 'products/products.html', context)


def product(request, pk):
    project_obj = Product.objects.get(id=pk)
    context = {
        'title': project_obj.name,
        'product': project_obj,
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/product.html', context)
