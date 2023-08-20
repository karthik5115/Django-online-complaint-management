from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='profiles/pic', blank=True)
    head = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Complaints(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False)
    complaint_name = models.CharField(max_length=15)
    complaint_image = models.ImageField(
        upload_to='media/complaintpics', blank=False)
    complaint_description = models.TextField()
    city = models.CharField(max_length=40)
    location = models.TextField(default='null')
    phone = models.DecimalField(decimal_places=0, max_digits=10)
    likes = models.DecimalField(decimal_places=0, max_digits=10, default=0)
    dislikes = models.DecimalField(decimal_places=0, max_digits=10, default=0)
    solved = models.BooleanField(default=False)
    liked_users = models.ManyToManyField(
        User, blank=True, related_name='liked_complaints')
    disliked_users = models.ManyToManyField(
        User, blank=True, related_name='disliked_complaints')

    def __str__(self):
        return self.complaint_name
# Create your models here.
