from django.core.management.base import BaseCommand
from store.models import Book
import random


class Command(BaseCommand):
    help = 'Creates sample books with ratings for demonstration'

    def handle(self, *args, **options):
        sample_books = [
            {
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'description': 'The story of the mysterious millionaire Jay Gatsby and his obsession with the beautiful Daisy Buchanan.',
                'price': '12.99',
                'stock': 25,
                'rating': 4.5
            },
            {
                'title': 'To Kill a Mockingbird',
                'author': 'Harper Lee',
                'description': 'The story of racial injustice and the destruction of innocence in a small Southern town.',
                'price': '10.99',
                'stock': 18,
                'rating': 4.8
            },
            {
                'title': '1984',
                'author': 'George Orwell',
                'description': 'A dystopian novel set in a totalitarian society ruled by the Party, which has total control over every aspect of people\'s lives.',
                'price': '9.99',
                'stock': 15,
                'rating': 4.6
            },
            {
                'title': 'The Catcher in the Rye',
                'author': 'J.D. Salinger',
                'description': 'The story of teenage protagonist Holden Caulfield and his experiences in New York City.',
                'price': '11.50',
                'stock': 12,
                'rating': 4.2
            },
            {
                'title': 'Pride and Prejudice',
                'author': 'Jane Austen',
                'description': 'A romantic novel about the Bennet family, focusing on the relationship between Elizabeth Bennet and Mr. Darcy.',
                'price': '8.99',
                'stock': 20,
                'rating': 4.7
            },
            {
                'title': 'The Hobbit',
                'author': 'J.R.R. Tolkien',
                'description': 'The adventure of home-loving Bilbo Baggins, who is reluctantly persuaded to join a company of dwarves on a journey to raid the treasure hoard of Smaug the dragon.',
                'price': '14.99',
                'stock': 30,
                'rating': 4.9
            },
            {
                'title': 'The Alchemist',
                'author': 'Paulo Coelho',
                'description': 'A novel about a young Andalusian shepherd named Santiago who travels to Egypt after having a recurring dream of finding treasure there.',
                'price': '9.50',
                'stock': 22,
                'rating': 4.4
            },
            {
                'title': 'The Lord of the Rings',
                'author': 'J.R.R. Tolkien',
                'description': 'An epic high-fantasy novel about the quest to destroy the One Ring, which was created by the Dark Lord Sauron.',
                'price': '29.99',
                'stock': 10,
                'rating': 4.9
            },
            {
                'title': 'Harry Potter and the Sorcerer\'s Stone',
                'author': 'J.K. Rowling',
                'description': 'The first novel in the Harry Potter series, featuring a young wizard, Harry Potter, and his friends at Hogwarts School of Witchcraft and Wizardry.',
                'price': '15.99',
                'stock': 35,
                'rating': 4.8
            },
            {
                'title': 'The Da Vinci Code',
                'author': 'Dan Brown',
                'description': 'A mystery thriller about symbologist Robert Langdon and cryptologist Sophie Neveu after a murder in the Louvre Museum in Paris.',
                'price': '13.50',
                'stock': 0,  # Out of stock for testing
                'rating': 3.9
            }
        ]

        # Clear existing books
        Book.objects.all().delete()
        self.stdout.write('Deleted existing books')

        # Create new books
        for book_data in sample_books:
            Book.objects.create(**book_data)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(sample_books)} sample books')) 