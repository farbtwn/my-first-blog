from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

#this is defining a class & its properties
class Post(models.Model):
  author = models.ForeignKey('auth.User', default = 'farbtwn')
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(
    default=timezone.now)
  published_date = models.DateTimeField(
    blank = True, null = True)
  
  
#these are the methods for this class(Post); they modify or act on the class they are a part of (Post)
  def publish(self):
    self.published_date = timezone.now()
    self.save()
  
  def __str__(self):
    return self.title
  #self makes the method act on the current instance of the object
  #class Duck()
    #color = 'blue striped'
    