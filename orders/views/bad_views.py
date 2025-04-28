from django.shortcuts import render
from orders.models import Customer, Product, Order


def bad_product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'orders/product_list.html', context)


def bad_order_list(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'orders/order_list.html', context)


def bad_customer_list(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'orders/customer_list.html', context)


def bad_order_detail_list(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'orders/order_detail_list.html', context)
