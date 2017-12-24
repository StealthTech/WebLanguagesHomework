from django.db import models

# Create your models here.


class Faculty(models.Model):
    class Meta:
        verbose_name = 'факультет'
        verbose_name_plural = 'факультеты'

    title = models.CharField(max_length=128, verbose_name='название', unique=True)
    short_title = models.CharField(max_length=16, verbose_name='сокращение', unique=True)

    def __str__(self):
        return self.title


class Department(models.Model):
    class Meta:
        verbose_name = 'кафедра'
        verbose_name_plural = 'кафедры'

    title = models.CharField(max_length=128, verbose_name='название', unique=True)
    index = models.IntegerField(verbose_name='Индекс', unique=True)
    faculty = models.ForeignKey('core.Faculty', on_delete=models.CASCADE, verbose_name='факультет')

    def __str__(self):
        return self.combined_title

    @property
    def short_title(self):
        return '{}{}'.format(self.faculty.short_title, self.index)

    @property
    def combined_title(self):
        return '{} {}'.format(self.short_title, self.title)


class Group(models.Model):
    class Meta:
        verbose_name = 'учебная группа'
        verbose_name_plural = 'учебные группы'
        unique_together = ['index', 'department']

    index = models.IntegerField(verbose_name='индекс группы')
    department = models.ForeignKey('core.Department', on_delete=models.CASCADE, verbose_name='кафедра', null=True)

    def __str__(self):
        return self.title

    @property
    def title(self):
        return '{}-{}'.format(self.department.short_title, self.index)


class Student(models.Model):
    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'

    first_name = models.CharField(max_length=255, verbose_name='имя')
    last_name = models.CharField(max_length=255, verbose_name='фамилия')
    group = models.ForeignKey(
        'core.Group', on_delete=models.PROTECT, verbose_name='учебная группа', blank=True, null=True)
    birth_date = models.DateField(verbose_name='дата рождения')
    current_disciplines = models.ManyToManyField(
        'core.Discipline', verbose_name='сейчас изучает', blank=True)

    def __str__(self):
        return 'Студент №{}. {} / Группа {}'.format(
            self.pk, self.get_full_name(), self.group.title if self.group else 'отсутствует')

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Discipline(models.Model):
    class Meta:
        verbose_name = 'дисциплина'
        verbose_name_plural = 'дисциплины'

    title = models.CharField(max_length=255, verbose_name='название')

    def __str__(self):
        return self.title

