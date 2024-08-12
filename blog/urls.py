from django.urls import path

from .views import HomeTemplateView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView

app_name = 'blog'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='index'),

    path('create/post/', PostCreateView.as_view(), name='create_post'),
    path('update/<slug:post_slug>/', PostUpdateView, name='update_post'),
    path('post/<slug:post_slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/delete/<slug:post_slug>/', PostDeleteView.as_view(), name='post_delete'),

    path('category/<slug:category_slug>/', HomeTemplateView.as_view(), name='category_filter'),
]
