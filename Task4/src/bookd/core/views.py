from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse

book_list = [
    {'pk': 1, 'title': 'Пикник на обочине', 'author': 'Братья Стругацкие'},
    {'pk': 2, 'title': 'Понедельник начинается в субботу', 'author': 'Братья Стругацкие'},
    {'pk': 3, 'title': 'Мастер и Маргарита', 'author': 'Булгаков М.А.'},
    {'pk': 4, 'title': 'Приключения Ийона Тихого', 'author': 'Станислав Лем'},
]


class IndexView(TemplateView):
    http_method_names = ['get']
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['book_list'] = book_list
        return context


class BookDetailsView(TemplateView):
    http_method_names = ['get']
    template_name = 'core/book_details.html'

    def get_context_data(self, **kwargs):
        context = super(BookDetailsView, self).get_context_data(**kwargs)
        book_pk = kwargs.get('pk')

        for elem in book_list:
            if elem.get('pk') == book_pk:
                context['book'] = elem
        return context
