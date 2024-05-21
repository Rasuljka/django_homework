from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, BlogWritingCreateView, BlogWritingDetailView, BlogWritingListView, BlogWritingUpdateView, \
    BlogWritingDeleteView, ContactTemplateView, HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('blogwrite/', BlogWritingCreateView.as_view(), name='blogwrite'),
    path('blogwrite/<int:pk>', BlogWritingDetailView.as_view(), name='blogwrite_read'),
    path('blogwrite/readall', BlogWritingListView.as_view(), name='blogwrite_readall'),
    path('blogwrite/edit/<int:pk>', BlogWritingUpdateView.as_view(), name='blogwrite_edit'),
    path('blogwrite/delete/<int:pk>', BlogWritingDeleteView.as_view(), name='blogwrite_delete')
]
