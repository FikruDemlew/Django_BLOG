from django.db import models
from PIL import Image
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isPublished = models.BooleanField(default=False)
    number_of_views = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to='blog_images', null=True, blank=True)
    
def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        img = img.resize((800, 600))

        img.save(self.image.path)