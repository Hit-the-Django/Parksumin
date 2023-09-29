from django.db import models

# Create your models here.
class Post(models.Model):
    phone_number = models.CharField('전화번호',max_length = 15)
    content = models.TextField('내용' ,default='비어있습니다 내용을 작성해주세요')
    student_number = models.IntegerField('학번')
    email = models.EmailField('이메일')