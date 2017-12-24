from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('student/<int:pk>/', views.StudentDetailsView.as_view(), name='student_details'),
    path('group/<int:pk>/', views.GroupDetailsView.as_view(), name='group_details'),
    # path('discipline/<int:pk>/', views.BookDetailsView.as_view(), name='discipline_details')
]
