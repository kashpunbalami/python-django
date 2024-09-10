from django.contrib import admin
from crud_app.models import Student, Author, Book, BorrowRecord

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phone_number')

admin.site.register(Student,StudentAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','biography')
    search_fields=('name','biography')

admin.site.register(Author,AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','published_date','isbn','available')
    list_filter=('available','author')
    search_fields=('title','author__name','isbn')
    ordering=('title',)

admin.site.register(Book,BookAdmin) 

class BorrowRecordAdmin(admin.ModelAdmin):
    list_display=('book','borrower','borrow_date','return_date')
    search_fields=('book__title','borrower__first_name')

admin.site.register(BorrowRecord,BorrowRecordAdmin)