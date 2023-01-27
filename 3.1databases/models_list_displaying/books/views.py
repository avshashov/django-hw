from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from datetime import datetime


def books_view(request):
    template = 'books/books_list_new.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def pub_date_view(request, pub_date):
    pub_date = datetime.strptime(pub_date, '%Y-%m-%d')
    book = Book.objects.filter(pub_date=pub_date)
    if not book:
        return HttpResponse(f'Публикаций за {pub_date.strftime("%Y-%m-%d")} не найдено.')
    else:
        books = Book.objects.all()
        paginator = Paginator(books, 1)
        current_page = request.GET.get('page', 1)
        page = paginator.get_page(current_page)

        context = {
            'books': page.object_list,
            'page': page,
        }
        return render(request, 'books/books_paginator.html', context)
