
from django.shortcuts import render
from orders.models import Customer, Product, Order, OrderItem


def show_database_info(request):
    products = Product.objects.count()
    orders = Order.objects.count()
    customers = Customer.objects.count()
    order_items = OrderItem.objects.count()

    context = {
        'product_count': products,
        'order_count': orders,
        'customer_count': customers,
        'order_item_count': order_items,
    }
    return render(request, 'orders/show_database_info.html', context)
