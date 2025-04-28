from django.core.management.base import BaseCommand
from orders.models import Customer, Product, Order, OrderItem
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Crea datos de prueba: Customers, Products, Orders y OrderItems'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Crear Productos
        products = []
        for _ in range(20):
            product = Product(
                name=fake.unique.word().capitalize(),
                price=round(random.uniform(10, 2000), 2),
                stock=random.randint(0, 100),
                # Mayor probabilidad de estar activos
                active=random.choice([True, True, True, False])
            )
            products.append(product)
        Product.objects.bulk_create(products)
        products = list(Product.objects.all())  # Refrescar con IDs

        self.stdout.write(self.style.SUCCESS('✅ 20 productos creados.'))

        # Crear Clientes
        customers = []
        for _ in range(30):
            customer = Customer(
                name=fake.name(),
                email=fake.unique.email(),
                is_active=fake.boolean(chance_of_getting_true=80)
            )
            customers.append(customer)
        Customer.objects.bulk_create(customers)
        customers = list(Customer.objects.all())  # Refrescar con IDs

        self.stdout.write(self.style.SUCCESS('✅ 30 clientes creados.'))

        # Crear Órdenes y OrderItems
        orders_to_create = []
        order_items_to_create = []

        for customer in customers:
            for _ in range(random.randint(1, 5)):  # 1 a 5 órdenes por cliente
                order = Order(customer=customer)
                orders_to_create.append(order)

        Order.objects.bulk_create(orders_to_create)
        orders = list(Order.objects.all())  # Refrescar

        for order in orders:
            selected_products = random.sample(
                products, random.randint(1, 3))  # 1 a 3 productos por orden
            for product in selected_products:
                quantity = random.randint(1, 5)
                order_item = OrderItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_items_to_create.append(order_item)

        OrderItem.objects.bulk_create(order_items_to_create)

        self.stdout.write(self.style.SUCCESS(
            '✅ Órdenes y order items creados exitosamente.'))
        self.stdout.write(self.style.SUCCESS('🎉 ¡Datos de prueba listos!'))
