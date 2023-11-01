from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(verbose_name='이미지')
    email = models.EmailField('이메일')
    contentn = models.TextField('내용')
    created_at = models.DateTimeField('작성일')
    