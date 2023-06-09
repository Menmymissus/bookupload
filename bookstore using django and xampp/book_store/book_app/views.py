from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
from django.shortcuts import redirect, get_object_or_404
# Create your views here.

def home(request):
    return render(request, 'home.html')

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete_book()
    return redirect('book_list')

def book_list(request):
    return render(request, 'book_list.html')

def book_list(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    books = Book.objects.all()
    context = {
        'form': form,
        'books': books
    }
    return render(request, 'book_list.html', context)

def edit_book(request, book_id):
    # Retrieve the book object using the book_id
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            # Redirect to the book list page
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'form': form, 'book': book})

