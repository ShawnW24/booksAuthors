from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('createBook',views.createBook),
    path('books/<int:bookid>',views.showBook),
    path('addAuthorToBook/<int:bookid>',views.addAuthorToBook),
    path('delete/<int:bookid>',views.deleteBook),
    path('edit/<int:bookid>',views.editBook),
    path('update/<int:bookid>',views.updateBook),
]
