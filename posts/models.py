from tokenize import blank_re
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=20,
        db_index=True
    )
    body = models.CharField(
        'Body', blank=True, null=True, max_length=140,
        db_index=True
    )
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )

    like_count = models.PositiveIntegerField(
        'like_count', blank = True, default=0
    )

    image = CloudinaryField('image', null= True, blank=True)
