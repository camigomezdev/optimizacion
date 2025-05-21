
from django.shortcuts import render
from django.db.models import Count, Q, Avg, F
from orders.models import Customer, Product, Order


def good_product_list(request):
    products = Product.objects.only('name', 'price').filter(stock__gte=0)

    avg_price = Product.objects.aggregate(avg_price=Avg('price'))['avg_price']

    context = {
        'avg_price': avg_price,
        'products': products
    }
    return render(request, 'orders/product_list.html', context)


def good_order_list(request):
    orders = Order.objects.select_related('customer').all()
    context = {'orders': orders}
    return render(request, 'orders/order_list.html', context)


def good_customer_list(request):
    customers = Customer.objects.annotate(
        order_count=Count('orders')
    ).prefetch_related('orders').all()
    context = {'customers': customers}
    return render(request, 'orders/customer_list.html', context)


def good_order_detail_list(request):
    orders = Order.objects.prefetch_related('items__product').all()
    context = {'orders': orders}
    return render(request, 'orders/order_detail_list.html', context)
