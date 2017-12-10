from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('books/<int:pk>/', views.BookDetailsView.as_view(), name='book_details')
]
