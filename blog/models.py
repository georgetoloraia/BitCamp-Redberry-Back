from django.db import models

class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    text_color = models.CharField(max_length=30)
    background_color = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField()
    description = models.TextField()
    image = models.URLField(max_length=200)
    categories = models.ManyToManyField(CategoryModel)
    email = models.EmailField(max_length=254, blank=True, null=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class UserModel(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
