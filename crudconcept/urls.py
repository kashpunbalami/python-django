"""
URL configuration for crudconcept project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from crud_app.views import add_student
from crud_app.views import student_list
from crud_app.views import update_student
from crud_app.views import test_url_resolve
from crud_app.views import delete_student
from crud_app.views import register
from crud_app.views import home
from crud_app.views import library_home, book_list, book_detail, add_book, edit_book, delete_book, add_author, delete_author, real_home, borrow_book, return_book


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', real_home, name="real_home"),
    path('home/', home, name="home"),
    path('add_student/', add_student, name="add_student"),
    path('student_list/', student_list, name="student_list"),
    path('update_student/<int:student_id>/', update_student, name="update_student"),
    path('test_url_resolve/', test_url_resolve, name="test_url_resolve"),
    path('delete_student/<int:student_id>/', delete_student, name="delete_student"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('register/', register, name="register"), 
    path('library/', library_home, name="library_home"),
    path('library/books/', book_list, name='book_list'),
    path('library/books/<int:pk>/', book_detail, name='book_detail'),
    path('library/books/add/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('library/books/<int:pk>/delete/', delete_book, name='delete_book'),
    path('library/author/', add_author, name="add_author"),
    path('library/author/<int:pk>/delete/', delete_author, name='delete_author'),
    path('borrow_book/', borrow_book, name="borrow_book"),
    path('return_book/<int:pk>/', return_book, name="return_book"),
]




