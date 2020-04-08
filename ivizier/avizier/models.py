from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Video 5 sa vad cum adaug datele aici
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # cand a fost create
    date = models.DateTimeField(default=timezone.now)
    # delete the post if the user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

