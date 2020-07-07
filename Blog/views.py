from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .models import Like

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  CreateView,
                                  DeleteView,
                                  DetailView,
                                  UpdateView )


class PostUpdateView(UpdateView, LoginRequiredMixin):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(DeleteView,  UserPassesTestMixin, LoginRequiredMixin):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"


class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['like'] = Like.objects.all()
        return context


def like_post(request, id):
    if request.user.is_authenticated:
        post = Post.objects.get(id=id)
        user = post.like_set.filter(user=request.user)
        if not user:
            post.like_set.create(user=request.user)
            post.save()

        else:
            Like.objects.filter(user=request.user, post=post).delete()
    return redirect('blog-home')


def home(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})


