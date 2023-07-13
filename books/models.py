from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    isbn = models.CharField(max_length=17)
    price = models.IntegerField()
    photo = models.ImageField(upload_to="books/", default="books/cover.png")

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    bio = models.TextField()
    email = models.EmailField()


class BookAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Reviews(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    review = models.TextField()
    stars_given = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
