from django import forms

from blog.models import Post, Category


class CreatePostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-select'}))

    PUBLISHED = "PUBLISHED"
    DRAFT = "DRAFT"
    _IS_PUBLISHED = [(PUBLISHED, 'Опубликовать'), (DRAFT, 'Черновик')]
    is_published = forms.ChoiceField(choices=_IS_PUBLISHED, widget=forms.Select(attrs={'class': 'form-select'}))

    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        exclude = ('author', 'count_views', 'slug', 'updated_at')


class UpdatePostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-select'}))

    PUBLISHED = "PUBLISHED"
    DRAFT = "DRAFT"
    _IS_PUBLISHED = [(PUBLISHED, 'Опубликовать'), (DRAFT, 'Черновик')]
    is_published = forms.ChoiceField(choices=_IS_PUBLISHED, widget=forms.Select(attrs={'class': 'form-select'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        exclude = ('author', 'count_views', 'slug', 'updated_at')

