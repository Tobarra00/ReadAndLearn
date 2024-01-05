import os
import json
from django.core.management.base import BaseCommand
from LibraryApp.models import Author, Book

class Command(BaseCommand):
    
    help = 'Loads new books from json file'

    def handle(self, *args, **options):

        path = os.path.join('books.json')
        try:
            with open(path, "r") as books:
                data = json.load(books)
                
                for book in data:
                    isbn=book['book']['ISBN']
                    existing_book = Book.objects.filter(isbn=isbn).first()

                    if existing_book is None:
                        author = Author.objects.create(
                            name=book['book']['author']['name'],
                            other_books=book['book']['author']['otherBooks']
                        )
                        Book.objects.create(
                            title=book['book']['title'],
                            isbn=isbn,
                            genre=book['book']['genre'],
                            pages=book['book']['pages'],
                            synopsis=book['book']['synopsis'],
                            cover=book['book']['cover'],
                            year=book['book']['year'],
                            author=author
                        )
                        self.stdout.write(self.style.SUCCESS(f'Loaded book: {book["book"]["title"]}'))
                    else:
                        self.stdout.write(self.style.NOTICE(f'Book already exists: {book["book"]["title"]}'))
        except FileNotFoundError:
            self.stdout.write(self.style.NOTICE("File not found. It may not be in the right directory. It should be at the same directory level as 'manage.py'"))
    