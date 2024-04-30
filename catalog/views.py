from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from pytils.translit import slugify
from .models import Product, BlogWriting


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def contacts(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            print(f'{name} ({email}): {message}')
            return render(request, self.template_name)


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "price", "category", "image")
    success_url = reverse_lazy("catalog:products")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "price", "category", "image")
    success_url = reverse_lazy('catalog:products')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products")


class BlogWritingCreateView(CreateView):
    model = BlogWriting
    fields = (
        'title', 'context', 'image',)
    success_url = reverse_lazy('catalog:blogwrite_readall')

    def form_valid(self, form):
        if form.is_valid:
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogWritingDetailView(DetailView):
    model = BlogWriting

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_of_views += 1
        self.object.save()
        return self.object


class BlogWritingListView(ListView):
    model = BlogWriting

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogWritingUpdateView(UpdateView):
    model = BlogWriting
    fields = (
        'title', 'context', 'image',)

    def get_success_url(self):
        return reverse_lazy('catalog:blogwrite_read', kwargs={'pk': self.object.pk})


class BlogWritingDeleteView(DeleteView):
    model = BlogWriting
    success_url = reverse_lazy('catalog:blogwrite_readall')
