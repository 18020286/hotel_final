from django.conf import settings
from django.db import models
from django_mysql.models import ListCharField
from user.models import User
from django_userforeignkey.models.fields import UserForeignKey


class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog')
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    TAG = (
        ('travel', 'Travel'),
        ('services', 'Services'),
        ('food', 'Food')
    )
    category = models.CharField(choices=TAG, max_length=8, default='travel')

    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.title
