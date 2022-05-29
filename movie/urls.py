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
    path("package", views.package_view, name='package'),
    path("mybooks", views.MyBooksListView.as_view(), name='mybooks'),
    path("account-info", views.AccountInfoListView.as_view(), name="info"),
    path("newbooks/", views.MyBookCreateView.as_view(), name="create"),
    # Book detail 
    path("book/<slug:slug>/", views.BookDetailView.as_view(), name='detail')
]