from django.test import TestCase
from .models import Book
from django.contrib.auth import get_user_model
# Create your tests here.


class TestBook(TestCase):
    def setUp(self):
        get_user_model().objects.create_user(
            username = 'kalycodes',
            email='kalycodes@gmail.com',
            password='c9mxQKJ*!T'
        )

        self.user = get_user_model().objects.get(id=1)

        Book.objects.create(
            author=self.user,
            title='Python',
            body = "I'm learning Python",
        )

        self.book = Book.objects.get(id=1)

    def test_book(self):
        self.assertEqual(self.book.author, self.user)
        self.assertEqual(f'{self.book.title}', 'Python')
        self.assertEqual(f'{self.book.body}', "I'm learning Python")