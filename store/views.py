from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Book
from django.conf import settings


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        book_count = books.count()
        debug_info = {
            'book_count': book_count,
            'connection_info': settings.DATABASES['default']
        }
        return render(request, 'store/book_list.html', {
            'books': books,
            'debug_info': debug_info
        })


class BookDetailView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'store/book_detail.html', {'book': book})


# Admin views
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class AdminBookListView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'admin/book_list.html', {'books': books})


class AdminBookAddView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request):
        return render(request, 'admin/book_form.html')
    
    def post(self, request):
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        cover_image = request.FILES.get('cover_image')
        
        if not all([title, author, description, price, stock]):
            return render(request, 'admin/book_form.html', {
                'error': 'All fields are required',
                'form_data': request.POST
            })
        
        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            return render(request, 'admin/book_form.html', {
                'error': 'Price must be a number and stock must be an integer',
                'form_data': request.POST
            })
            
        book = Book(
            title=title,
            author=author,
            description=description,
            price=price,
            stock=stock,
            cover_image=cover_image
        )
        book.save()
        
        return redirect('admin_books')


class AdminBookEditView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'admin/book_form.html', {'book': book})
    
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        cover_image = request.FILES.get('cover_image')
        
        if not all([title, author, description, price, stock]):
            return render(request, 'admin/book_form.html', {
                'error': 'All fields are required',
                'book': book,
                'form_data': request.POST
            })
        
        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            return render(request, 'admin/book_form.html', {
                'error': 'Price must be a number and stock must be an integer',
                'book': book,
                'form_data': request.POST
            })
            
        book.title = title
        book.author = author
        book.description = description
        book.price = price
        book.stock = stock
        
        if cover_image:
            book.cover_image = cover_image
            
        book.save()
        
        return redirect('admin_books')


class AdminBookDeleteView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'admin/book_confirm_delete.html', {'book': book})
    
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect('admin_books') 