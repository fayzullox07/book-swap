from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import DeleteView, UpdateView#, CreateView
from django.http import HttpResponseRedirect
from . import models
from .forms import *

# Create your views here.


def home_view(request):
    return render(request, "index.html")



def genres_view(request):
    return render(request, "genres.html")



class PostListView(ListView):
    model = models.Book
    template_name = "posts.html"

class PostLoveListView(ListView):
    model = models.Book
    template_name = "lovebook.html"

class MyBooksListView(ListView):
    model = models.Book
    template_name = "my_book.html"


class GenreListView(ListView):
    model = models.Genre
    template_name = "genres.html"



class BookDetailView(View):
    def get(self, request, slug):
        model = models.Book.objects.all
        books = models.Book.objects.get(slug=slug)
        return render(request,"detail.html", {"books":books,"model":model})



class MyBooksDetailView(View):
    def get(self, request, slug):
        model = models.Book.objects.all
        books = models.Book.objects.get(slug=slug)
        return render(request,"my-book-details.html", {"books":books,"model":model})





# class MyBookCreateView(CreateView):
#     model = models.Book
#     template_name = "package.html"
#     form_class = AddTodoForm
#     success_url = "/books"


def addBook(request):
    print(request.POST.get("src"))

    if request.method == "POST":
        form = AddTodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/books")
    else:
        form = AddTodoForm()
    return render(request, "package.html", {"form": form})



class EditTodoView(UpdateView):
    model = Book
    template_name = "edit.html"
    success_url = '/mybooks'
    fields = "__all__"


class DeleteTodoView(DeleteView):
    model = Book
    success_url = '/books'

# Create def