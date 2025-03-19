from django.db import models

from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
import os
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    completed_image = models.ImageField(upload_to='completed_images/', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True, default='default_thumbnail.jpg')

    def save(self, *args, **kwargs):
        if self.completed_image:
            img_path = self.completed_image.path
            img = Image.open(img_path)
            
            # Resize the image to make a thumbnail
            thumbnail_name = f"{os.path.splitext(os.path.basename(img_path))[0]}_thumbnail.jpg"
            thumbnail_path = os.path.join(settings.MEDIA_ROOT, 'thumbnails', thumbnail_name)
            
            img.thumbnail((100, 100))
            img.save(thumbnail_path)

            self.thumbnail = os.path.join('thumbnails', thumbnail_name)

        super(Todo, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

