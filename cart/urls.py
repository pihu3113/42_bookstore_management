from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('add/<int:book_id>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('update/<int:book_id>/', views.UpdateCartView.as_view(), name='update_cart'),
    path('remove/<int:book_id>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
] 