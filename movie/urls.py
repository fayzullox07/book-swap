from django.urls import path
from django.contrib.auth import views as auth_views
from .import views




app_name= 'movie'

urlpatterns = [
    path("", views.home_view, name='home'),
    # Registration


     # Book detail
    path("genres", views.GenreListView.as_view(), name='genres'),
    path("books", views.PostListView.as_view(), name='books'),
    path("lovebook", views.PostLoveListView.as_view(), name='lovebook'),
    # path("package", views.MyBookCreateView, name='package'),
    path("mybooks", views.MyBooksListView.as_view(), name='mybooks'),
    path("mybookdetail/<slug:slug>/", views.MyBooksDetailView.as_view(), name='my_book_detail'),
    # Book detail 
    path("book/<slug:slug>/", views.BookDetailView.as_view(), name='detail'),

    # Book creating
    path("edit/<slug:slug>/", views.EditTodoView.as_view(), name="edit"),
    path("delete/<slug:slug>/", views.DeleteTodoView.as_view(), name="delete"),
    path("addbooks/", views.addBook, name="package"),

]