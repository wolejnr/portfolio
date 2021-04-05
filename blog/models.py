from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    blogdate = models.DateField()
    featured_image = models.ImageField(upload_to='post/images/')
    content = models.TextField()

    def __str__(self):
        return self.title