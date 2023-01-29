from django.db.models import F
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
        book = Book.objects.filter(pub_date=pub_date)
        next_page = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
        if next_page:
            next_page = next_page.pub_date.strftime('%Y-%m-%d')
        previous_page = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
        if previous_page:
            previous_page = previous_page.pub_date.strftime('%Y-%m-%d')
    context = {
        'book': book,
        'next_page': next_page,
        'previous_page': previous_page,
    }
    return render(request, 'books/books_paginator.html', context)
