
from django.urls import path

from .views import (
    ProductsIndexView, 
    OrdersIndexView, 
    task_status,
    create_category,
    CreateCategory,
    ListCategory,
    UpdateCategory,
    ReadCategory,
    ProductDetailView,
)
app_name ="store_app"

urlpatterns = [
    path("products/", ProductsIndexView.as_view(), name="products_index"),
    path("orders/", OrdersIndexView.as_view(), name="orders_index"),
    path("task_status/", task_status, name="task_status"),
    # path("category/create/", create_category, name="create_category"),
    path("category/create/", CreateCategory.as_view(), name="create_category"),
    path("category/update/<int:pk>/", UpdateCategory.as_view(), name="update_category"),
    path("category/<int:pk>/", ReadCategory.as_view(), name="read_category"),
    path("category/", ListCategory.as_view(), name="list_category"),
    path("product/<int:id>/", ProductDetailView.as_view(), name="product_detail"),
]

