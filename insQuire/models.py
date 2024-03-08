from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from .models import Tag, UserProfile
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    questionsInCategory = models.IntegerField()
    slugifiedName = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        self.slugifiedName = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Question(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    dateAsked = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
<<<<<<< HEAD


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
=======
    
class Answer(models.Model):
    content = models.TextField()
    dateAnswered = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.content
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    occurrences = models.IntegerField(default=0)

def __str__(self):
    return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.user.username


>>>>>>> 9228f391af5dfd1c7536e027aae8d176ff901376
