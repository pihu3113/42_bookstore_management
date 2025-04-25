from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='home'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('admin/books/', views.AdminBookListView.as_view(), name='admin_books'),
    path('admin/books/add/', views.AdminBookAddView.as_view(), name='admin_book_add'),
    path('admin/books/edit/<int:pk>/', views.AdminBookEditView.as_view(), name='admin_book_edit'),
    path('admin/books/delete/<int:pk>/', views.AdminBookDeleteView.as_view(), name='admin_book_delete'),
] 