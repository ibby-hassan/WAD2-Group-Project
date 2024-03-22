from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
    

#Helper model classes
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    occurrences = models.IntegerField(default=0)

def __str__(self):
    return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True, default='profile_images/default.jpg')
    website = models.URLField(blank=True)
                                      
    def __str__(self):
        return self.user.username


#The below models are related to displaying questions and answers on the website
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    questionCount = models.IntegerField(default=0)
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
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

        
    def __str__(self):
        return self.title
    
class Answer(models.Model):
    content = models.TextField()
    dateAnswered = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.content
    


