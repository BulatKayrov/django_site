from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView

from blog.blog_mixins import BackToListMixin, CategoryFilterMixin, TitleForObjectMixin
from blog.forms import CreatePostForm, UpdatePostForm
from blog.models import Post
from blog.tasks import send_email


# class PostUpdateView(UpdateView):
#     form_class = UpdatePostForm
#     # model = Post
#     slug_url_kwarg = 'post_slug'
#     template_name = 'blog/update_post.html'
#     success_url = reverse_lazy('blog:index')


def PostUpdateView(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    if request.method == 'POST':
        form = UpdatePostForm(data=request.POST, files=request.FILES, instance=post)
        if form.is_valid():
            print('form is valid')
            form.save()
            send_email.delay()
            return redirect('blog:index')
    else:
        form = UpdatePostForm(instance=post)
    context = {'form': form, 'post': post.slug}
    return render(request=request, template_name='blog/update_post.html', context=context)


class PostDeleteView(DeleteView):
    model = Post
    slug_url_kwarg = 'post_slug'

    def get_success_url(self):
        return reverse(viewname='user:profile', kwargs={'user_id': self.request.user.id})


class HomeTemplateView(CategoryFilterMixin, ListView):
    title = 'Главная'
    filter_name = 'category_slug'
    # model = Post
    queryset = Post.objects.select_related('category', 'author').all()
    paginate_by = 1
    template_name = 'blog/index.html'
    context_object_name = 'posts'


class PostDetailView(TitleForObjectMixin, BackToListMixin, DetailView):
    come_back = True
    # model = Post
    queryset = Post.objects.select_related('category', 'author').all()
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


class PostCreateView(CreateView):
    form_class = CreatePostForm
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)
