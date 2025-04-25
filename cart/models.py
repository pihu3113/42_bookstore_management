from django.db import models
from django.contrib.auth.models import User
from store.models import Book

# Cart will be session-based, but we'll define models for reference
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Order {self.id} - {self.user.username}"
    
    def get_total(self):
        items = self.orderitem_set.all()
        return sum(item.get_total for item in items)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.quantity} x {self.book.title}"
    
    @property
    def get_total(self):
        return self.book.price * self.quantity 