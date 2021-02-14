
from django.urls import path, include
from . import views
urlpatterns = [
    path('add_category/', views.AddCategory.as_view(), name='add_category'),
    path('list_categories/', views.ListCategories.as_view(), name='list_categories'),
    path('add_product/', views.AddProduct.as_view(), name='add_product'),
    path('list_products/', views.ListProducts.as_view(), name='list_products'),
    path('list_products/<int:cat_id>/', views.GetProductsByCategory.as_view(), name='list_category_products'),
    path('delete_category/<int:pk>/', views.DeleteCategoryById.as_view(), name='delete_category'),
]
