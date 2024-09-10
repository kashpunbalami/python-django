from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from crud_app.models import Student, Book, Author, BorrowRecord
from crud_app.forms import StudentForm, BookForm, AuthorForm, BorrowRecordForm
from django.urls import resolve
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q



# Create your views here.

@login_required
def add_student(request):
    n=''
    s = None
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        s=Student(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number)
        s.save()
        n="student saved"
    return render(request, "add_student.html", {'s':s, 'n':n})

@login_required
def student_list(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(phone_number__icontains=query)
        )
    else:
        students=Student.objects.all()
    context={
        'students':students
    }
    return render(request, 'student_list.html' , context)

@login_required
def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        else:
            return render(request, 'update_student.html', {'form': form, 'student':student})

    else:
        form = StudentForm(instance=student)
        return render(request, 'update_student.html', {'form': form, 'student':student})

def test_url_resolve(request):
    match = resolve('/update_student/1/')
    return HttpResponse(f"View: {match.view_name}")

@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'delete_Student.html', {'student': student})

@login_required
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def library_home(request):
    return render(request, 'library_home.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

def add_book(request):
    authors = Author.objects.all()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form, 'authors': authors})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    borrow_records = BorrowRecord.objects.filter(book=book)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book, 'borrow_records': borrow_records})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})

def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

def delete_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        author.delete()
        return redirect('book_list')
    return render(request, 'delete_author.html', {'author': author})

@login_required
def real_home(request):
    return render(request, 'real_home.html')

def borrow_book(request):
    if request.method == "POST":
        form = BorrowRecordForm(request.POST)
        if form.is_valid():
            borrow_record = form.save(commit=False)
            borrow_record.book.available = False
            borrow_record.book.save()
            borrow_record.save()
            return redirect('book_list')
    else:
        form = BorrowRecordForm()
    return render(request, 'borrow_book.html', {'form': form})

def return_book(request, pk):
    borrow_record = get_object_or_404(BorrowRecord, pk=pk)
    if request.method == "POST":
        borrow_record.return_date = request.POST.get('return_date')
        borrow_record.book.available = True
        borrow_record.book.save()
        borrow_record.save()
        return redirect('book_list')
    return render(request, 'return_book.html', {'borrow_record': borrow_record})
