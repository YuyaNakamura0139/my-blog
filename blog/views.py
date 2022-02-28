from re import template
from django.views.generic import DetailView, ListView, TemplateView
from blog.models import Post


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


class PostListView(ListView):
    model = Post
    ordering = "-created_at"
    template_name = "post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = "post_id"
    template_name = "post_detail.html"
    context_object_name = "post"
