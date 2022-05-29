from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView
from . import models
# Create your views here.


def home_view(request):
    return render(request, "index.html")



def genres_view(request):
    return render(request, "genres.html")

def package_view(request):
    return render(request, "package.html")

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

class AccountInfoListView(ListView):
    model = models.AccountInfo
    template_name = "personal-information.html"


class BookDetailView(View):
    def get(self, request, slug):
        model = models.Book.objects.all
        books = models.Book.objects.get(slug=slug)
        return render(request,"detail.html", {"books":books,"model":model})


class MyBookCreateView(CreateView):
    model = models.Book
    template_name = "package.html"
    fields = ['title', 'author', 'book_img', 'genre', 'city', 'time',"desc"]
