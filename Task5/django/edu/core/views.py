from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
from django.urls import reverse

from core.models import Student, Group, Discipline, Faculty

book_list = [
    {'pk': 1, 'title': 'Пикник на обочине', 'author': 'Братья Стругацкие'},
    {'pk': 2, 'title': 'Понедельник начинается в субботу', 'author': 'Братья Стругацкие'},
    {'pk': 3, 'title': 'Мастер и Маргарита', 'author': 'Булгаков М.А.'},
    {'pk': 4, 'title': 'Приключения Ийона Тихого', 'author': 'Станислав Лем'},
]


class IndexView(ListView):
    http_method_names = ['get']
    template_name = 'core/index.html'
    model = Faculty

    def get_queryset(self):
        queryset = self.model.objects.prefetch_related('department_set', 'department_set__group_set')
        return queryset


class StudentDetailsView(TemplateView):
    http_method_names = ['get']
    template_name = 'core/student_details.html'

    def get_context_data(self, **kwargs):
        context = super(StudentDetailsView, self).get_context_data(**kwargs)
        context['student'] = get_object_or_404(Student, pk=kwargs.get('pk'))
        return context


class GroupDetailsView(DetailView):
    http_method_names = ['get']
    template_name = 'core/group_details.html'
    model = Group
    context_object_name = 'group'
