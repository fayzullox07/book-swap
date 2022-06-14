from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

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
    # id = models.BigAutoField(
    #     auto_created=True, primary_key=True, serialize=False, verbose_name='ID',null=True,blank=True)
    title = models.CharField("Kitobni nomi",max_length=50)
    author = models.CharField("kitob aftori",max_length=50)
    slug = models.SlugField("kitob slugi",max_length=100,blank=True)
    # genre = models.ForeignKey(Genre)
    genre = models.CharField(max_length=50)
    src = models.ImageField(upload_to="gallery/%Y/%m/%d")
    time = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
    class Meta:
        """Meta definition for Book."""

        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        """Unicode representation of Book."""
        return f"{self.title}"

# class AccountInfo(models.Model):
#     GENDERS = (
#         ("erkak", "ERKAK"),
#         ("ayol", "AYOL"),
#         ("nomalum", "ANIQMAS"),
#     )

#     user = models.OneToOneField(
#         User, on_delete=models.CASCADE, related_name='profile')
#     name = models.CharField(max_length=50, blank=True)
#     surname = models.CharField(max_length=50, blank=True)
#     avatar = models.ImageField(
#         default='profile_images/smile.png', upload_to='profile_images/')
#     gender = models.CharField(max_length=10, choices=GENDERS, blank=True)
#     age = models.PositiveIntegerField(default=0)
#     address = models.CharField(max_length=100, blank=True)
#     bio = models.TextField(blank=True)

#     def __str__(self):
#         return self.user.username



class Comment(models.Model):
    """Model definition for Comment."""
    # book = models.ForeignKey(Book, on_delete=models.PROTECT,related_name="comments", null=True)
    # author = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name='user')    
    # comment = models.TextField()
    # TODO: Define fields here

    # class Meta:
    #     """Meta definition for Comment."""

    #     verbose_name = 'Comment'
    #     verbose_name_plural = 'Comments'
    #     ordering = ["-id"]

    # def __str__(self):
    #     """Unicode representation of Comment."""
    #     return f"{self.comment}"
    # def get_absolute_url(self):
 #     return reverse("books")
    pass    