from django.db import models

class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publish_date = models.DateTimeField()
    description = models.TextField()
    categories = models.ManyToManyField('CategoryModel')
    image = models.ImageField(upload_to='blogs/')

    def __str__(self):
        return self.title

class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    text_color = models.CharField(max_length=7)
    background_color = models.CharField(max_length=7)

    def __str__(self):
        return self.title

class UserModel(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
