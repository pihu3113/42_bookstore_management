from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from store.models import Book


class CartView(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        cart_items = []
        total = 0
        
        for book_id, quantity in cart.items():
            try:
                book = Book.objects.get(id=book_id)
                item_total = float(book.price) * int(quantity)
                total += item_total
                cart_items.append({
                    'book': book,
                    'quantity': quantity,
                    'total': item_total
                })
            except Book.DoesNotExist:
                # Remove invalid items from cart
                del cart[book_id]
                request.session['cart'] = cart
                
        return render(request, 'cart/cart.html', {
            'cart_items': cart_items,
            'total': total
        })


class AddToCartView(View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        quantity = int(request.POST.get('quantity', 1))
        
        # Initialize cart if not exists
        if 'cart' not in request.session:
            request.session['cart'] = {}
            
        cart = request.session['cart']
        
        # Add or update item in cart
        if str(book_id) in cart:
            cart[str(book_id)] = int(cart[str(book_id)]) + quantity
        else:
            cart[str(book_id)] = quantity
            
        request.session['cart'] = cart
        
        return redirect('cart')


class UpdateCartView(View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity <= 0:
            return redirect('remove_from_cart', book_id=book_id)
            
        if 'cart' in request.session:
            cart = request.session['cart']
            if str(book_id) in cart:
                cart[str(book_id)] = quantity
                request.session['cart'] = cart
                
        return redirect('cart')


class RemoveFromCartView(View):
    def get(self, request, book_id):
        if 'cart' in request.session:
            cart = request.session['cart']
            if str(book_id) in cart:
                del cart[str(book_id)]
                request.session['cart'] = cart
                
        return redirect('cart') 