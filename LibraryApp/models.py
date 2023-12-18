from autoslug import AutoSlugField
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model

# Create your models here.

class Author(models.Model):
    
    name = models.CharField(max_length=50, blank=False, null=False)
    other_books = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    
    def __str__(self) -> str:
        return self.name
    
class Book(models.Model):
    
    isbn = models.CharField(max_length=14, primary_key=True)
    title = models.CharField(max_length=60, blank=False, null=False)
    slug = AutoSlugField(populate_from='title', unique=True, null=True)
    genre = models.CharField(max_length=30, blank=False, null=False)
    pages = models.PositiveIntegerField(default=0, blank=False, null=False)
    synopsis = models.TextField(blank=False, null=False)
    year = models.IntegerField(default=0, blank=False, null=True)
    cover = models.URLField(blank=False, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    
    def __str__(self) -> str:
        return self.title
    
User = get_user_model()

class List(models.Model):
    
    name = models.CharField(max_length=50, null=False, blank=False)
    slug = AutoSlugField(populate_from='name', unique=True, null=True)
    description = models.TextField(blank=True, null=False)
    created = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    modified = models.DateTimeField(auto_now=True, blank=False, null=False)
    book = models.ManyToManyField(Book)
    user = models.ManyToManyField(User)
    shared_to = ArrayField(models.CharField(max_length=50), blank=True, default=list)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'List'
        verbose_name_plural = 'Lists'
    
    def __str__(self) -> str:
        return self.name
    
""" class BookListRelation(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('list', 'book') """

""" class SharedLists(models.Model):
    
    shared_list = models.ForeignKey(List, on_delete=models.CASCADE)
    shared_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_from')
    shared_to = models.ManyToManyField(User, related_name='shared_to')
    shared_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['shared_from']
        default_permissions = ('view',) """
