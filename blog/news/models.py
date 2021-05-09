
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    # Redirect to post details page
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
    def __repr__(self):
        return f'(Post) {self.title}'
        
    def __str__(self):
        return self.title
