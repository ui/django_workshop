from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    pub_date = models.DateTimeField()
    
    def __unicode__(self):
        return self.title