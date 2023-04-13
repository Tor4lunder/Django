from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('category/all', views.all_categories, name='all_categories'),
    path('category/<int:category_id>', views.category, name='category'),
    path('news/<int:news_id>', views.news_detail, name='news_detail'),
]