from django.urls import path
from . import views

app_name = 'categories'
urlpatterns = [
    path('', views.all_categories, name='all'),
    path('<slug:category_slug>', views.show_category, name='show'),
]
