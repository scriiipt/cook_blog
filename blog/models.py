
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    parent = TreeForeignKey(
        'self',
        related_name='children',
        on_delete=models.SET_NULL, 
        null=True,
        blank=True
    )

    class MPTTMeta:
        order_insertion_by = ['name']
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug' : self.slug})


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('post_single', kwargs={'tag_slug' : self.slug})


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/dishes/')
    text = models.TextField()
    slug = models.SlugField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(
        Category,
        related_name='post',
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(Tag, related_name='tags')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_single', kwargs={'slug':self.category.slug, 'post_slug':self.slug})
    

class Recipe (models.Model):
    name = models.CharField(max_length=100)
    serves = models.CharField(max_length=50)
    ingredients = RichTextField()
    directions = RichTextField()
    prep_time = models.PositiveIntegerField(default = 0)
    cook_time = models.PositiveIntegerField(default = 0)
    post = models.ForeignKey(Post,  verbose_name="recipe", on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name    
    

class Comments(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=700)
    massage = models.TextField(max_length=650)
    post = models.ForeignKey(Post, verbose_name='comment', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.email    
    
