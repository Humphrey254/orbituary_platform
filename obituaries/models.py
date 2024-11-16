from django.db import models

class Obituary(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='obituary_images/', null=True, blank=True)

    def __str__(self):
        return self.title

