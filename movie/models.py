from django.db import models
from django.forms import SlugField

# Create your models here.

class Genre(models.Model):
    slug = models.SlugField(max_length=100)
    name = models.CharField("Genre name", max_length=70)
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'



class Book(models.Model):
    """Model definition for Book."""

    # TODO: Define fields here
    title = models.CharField("Kitobni nomi",max_length=50)
    author = models.CharField("kitob aftori",max_length=50)
    slug = models.SlugField(max_length=100)
    genre = models.ManyToManyField(Genre)
    book_img = models.ImageField("Rasmi", upload_to="movie_posters/%Y/%m")
    city = models.CharField("SHahri", max_length=50, unique=True)
    time = models.CharField(max_length=50)
    desc = models.TextField()
    class Meta:
        """Meta definition for Book."""

        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        """Unicode representation of Book."""
        return f"{self.title}"

class AccountInfo(models.Model):
    name = models.CharField(max_length=50)
    sorename = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    number = models.PositiveIntegerField(default=+9983333333)
    def __str__(self):
        return f"{self.name}"


    class Meta:

        verbose_name = 'AccountInfo'
        verbose_name_plural = 'AccountInfos'