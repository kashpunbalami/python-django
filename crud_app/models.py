from django.db import models

# Create your models here.

class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name
    
class Author(models.Model):
    name=models.CharField(max_length=50)
    biography=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
        
class Book(models.Model):
    title=models.CharField(max_length=40)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date=models.DateField()
    isbn=models.CharField(max_length=13, unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class BorrowRecord(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower=models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    borrow_date=models.DateField(auto_now_add=True)
    return_date=models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.borrower}-{self.book.title}"