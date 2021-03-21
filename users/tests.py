from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.


class TestSignUp(TestCase):

    def setUp(self):
        get_user_model().objects.create_user(
            username = 'kalycodes',
            email='kalycodes@gmail.com',
            password='c9mxQKJ*!T'
        )

        self.user = get_user_model().objects.get(id=1)

    def test_username(self):
        self.assertEqual(f'{self.user.username}', 'kalycodes')

    def test_email(self):
        self.assertEqual(f'{self.user.email}', 'kalycodes@gmail.com')