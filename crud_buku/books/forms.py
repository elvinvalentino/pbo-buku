from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    title = forms.CharField(label='Judul', widget=forms.TextInput(attrs={'class': 'form-control'}))
    publisher = forms.CharField(label='Penerbit', widget=forms.TextInput(attrs={'class': 'form-control'}))
    author = forms.CharField(label='Penulis', widget=forms.TextInput(attrs={'class': 'form-control'}))
    genre = forms.CharField(label='Genre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    publication_date = forms.CharField(label='Tanggal Publish', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Book
        fields = ('title', 'publisher', 'author', 'genre', 'publication_date')