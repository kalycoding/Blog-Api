from django.test import TestCase
from .models import Post
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

        Post.objects.create(
            author=self.user,
            title='Python',
            body = "I'm learning Python",
        )

        self.post = Post.objects.get(id=1)

    def test_book(self):
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(f'{self.post.title}', 'Python')
        self.assertEqual(f'{self.post.body}', "I'm learning Python")