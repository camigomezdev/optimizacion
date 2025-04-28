from django.urls import path
from orders.views import views, bad_views, good_views

urlpatterns = [
    path('', views.show_database_info, name='bad_show_database_info'),
    
    # vistas sin optimizar
    path('bad-products/', bad_views.bad_product_list, name='bad_product_list'),
    path('bad-orders/', bad_views.bad_order_list, name='bad_order_list'),
    path('bad-customers/', bad_views.bad_customer_list,
         name='bad_customer_list'),
    path('bad-orders-details/', bad_views.bad_order_detail_list,
         name='bad_order_detail_list'),

    # vistas optimizadas
    path('good-products/', good_views.good_product_list,
         name='good_product_list'),
    path('good-orders/', good_views.good_order_list, name='good_order_list'),
    path('good-customers/', good_views.good_customer_list,
         name='good_customer_list'),
    path('good-orders-details/', good_views.good_order_detail_list,
         name='bad_order_detail_list'),
]
