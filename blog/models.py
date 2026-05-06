from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)


    def __str__(self):

        return self.name

    class Meta:

        verbose_name_plural = "Categories"



class Author(models.Model):
    name = models.CharField(max_length=200)


    email = models.EmailField(unique=True)


    bio = models.TextField(blank=True)


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()


    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='posts'

    )


    categories = models.ManyToManyField(
        Category,
        blank=True,
        related_name='posts'
    )


    created_at = models.DateTimeField(auto_now_add=True)


    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:

        ordering = ['-created_at']