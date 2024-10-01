from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# Create your views here.


def home(request):
    catalog_list = Product.objects.all()
    context = {"products": catalog_list}
    return render(request, "products_list.html", context)


def product_detail(request, pk):
    product_detail = get_object_or_404(Product, pk=pk)
    context = {"products": product_detail}
    return render(request, "product_detail.html", context)


def contacts(request):
    return render(request, "contacts.html")
