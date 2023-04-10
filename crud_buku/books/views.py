from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html',{'books': books})

def create_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
      form.save()
      return redirect('book_list')
    return render(request, 'book_form_create.html', {'form': form})

def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'book_form_update.html', {'form': form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_delete.html', {'book': book})

