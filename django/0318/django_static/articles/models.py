from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    image = ProcessedImageField( # 원본을 사용하지 않을 때 사용
        blank=True,
        processors=[Thumbnail(100, 100)], # 썸네일 크기
        format='JPEG', # jpeg 로 처리
        options={
            'quality': 80, # 기존 이미지를 80% 압축
        }
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title