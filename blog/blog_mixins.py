from django.core.cache import cache

from blog.models import Post


class BackToListMixin:
    come_back = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.come_back:
            context['back_to'] = self.request.META['HTTP_REFERER']
            return context
        return context


class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.title:
            context['title'] = self.title
        return context


class TitleForObjectMixin(TitleMixin):
    """
        Если нужно явно задать заголовок страницы воспользуйтесь атрибутом title, иначе он вернет title из get_object()
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.title:
            context['title'] = self.object.title
        return context


class CategoryFilterMixin(TitleMixin):
    filter_name = None

    def get_queryset(self):

        queryset = super().get_queryset()
        _category = self.kwargs.get(self.filter_name)
        if _category:
            queryset = queryset.filter(category__slug=_category)
        return queryset

    def get_paginate_by(self, queryset):
        # если страница не главная, то выводим все посты
        if self.request.META['PATH_INFO'] != '/':
            return self.paginate_by
        return None
