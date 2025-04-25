import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()

# Now we can import Django models
from store.models import Book

def check_connection():
    try:
        # Try to count books
        book_count = Book.objects.count()
        print(f"Successfully connected to the database. Found {book_count} books.")
        
        # List books if any
        if book_count > 0:
            print("\nBooks in the database:")
            for i, book in enumerate(Book.objects.all(), 1):
                print(f"{i}. {book.title} by {book.author} - ${book.price} (Rating: {book.rating})")
        else:
            print("\nNo books found in the database.")
            
        return True
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return False

if __name__ == "__main__":
    print("Checking MySQL database connection...")
    check_connection() 