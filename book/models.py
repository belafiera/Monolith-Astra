from django.db import models


# Create your models here.
from django.urls import reverse


class User(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    his_reviews = models.ForeignKey('Review', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Book(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=70)
    description = models.TextField(blank=True)
    user_rating = models.FloatField()
    critique_rating = models.FloatField()
    cover_picture = models.ImageField(upload_to="covers/%Y/%m/%d/")
    author_of = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)
    users_review = models.ForeignKey('Review', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + ' ' + ', Genre: ' + self.genre

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Review(models.Model):
    the_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    review_text = models.TextField()
    books_review = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    collection = models.ManyToManyField(Book)
    picture = models.ImageField(upload_to="auth_pic/%d/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Library(models.Model):
    name = models.CharField(max_length=100)
    available_books = models.ManyToManyField(Book)
    address = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
