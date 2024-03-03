from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title