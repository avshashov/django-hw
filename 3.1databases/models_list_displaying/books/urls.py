from django.urls import path

from .views import books_view, pub_date_view

urlpatterns = [
    path('books/', books_view, name='books'),
    path('books/<pub_date>', pub_date_view, name='pub_date'),
]
