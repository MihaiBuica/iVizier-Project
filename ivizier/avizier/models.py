from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


# Video 5 sa vad cum adaug datele aici
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # cand a fost create
    date = models.DateTimeField(default=timezone.now)
    # delete the post if the user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='events')

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        size = 250
        if img.height > size or img.width > size:
            output_size = (size, size)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})