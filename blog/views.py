from django.views.generic import ListView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-pk'

