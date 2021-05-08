from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model
from rest_framework import test
from .views import PostListCreateAPI, PostRetrieveUpdateDelete
# Create your tests here.


# class TestBook(TestCase):
#     def setUp(self):
#         get_user_model().objects.create_user(
#             username = 'kalycodes',
#             email='kalycodes@gmail.com',
#             password='c9mxQKJ*!T'
#         )

#         self.user = get_user_model().objects.get(id=1)

#         Post.objects.create(
#             author=self.user,
#             title='Python',
#             body = "I'm learning Python",
#         )

#         self.post = Post.objects.get(id=1)

#     def test_book(self):
#         self.assertEqual(self.post.author, self.user)
#         self.assertEqual(f'{self.post.title}', 'Python')
#         self.assertEqual(f'{self.post.body}', "I'm learning Python")

class TestEndPoints(TestCase):
    def setUp(self):
        self.factory = test.APIRequestFactory()
        self.view = PostListCreateAPI.as_view()

        

    def test_post_books_endpoints(self):
        request = self.factory.post('/api/v1/post/', {'title':'Python', 'body':'Im learning Python'}, format='json')
        # test.force_authenticate(request, token='e5c5c86e6f8ecab26b01577e9554170c340dd601')
        response = self.view(request)
        response.render()
        self.assertEqual(response.status_code, 201)

    def test_get_books_endpoints(self):
        request = self.factory.get('/api/v1/post/')
        # test.force_authenticate(request, token='e5c5c86e6f8ecab26b01577e9554170c340dd601')
        response = self.view(request)
        response.render()
        self.assertEqual(response.status_code, 200)