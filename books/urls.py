from django.urls import path
from .views import PostListCreateAPI, PostRetrieveUpdateDelete

urlpatterns = [
    path('post/', PostListCreateAPI.as_view()),
     path('post/<int:pk>/', PostRetrieveUpdateDelete.as_view())
]
