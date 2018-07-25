from django.db import models
from django.utils import timezone


#객체(모델)정의
class Post(models.Model):          
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #다른 모델 링크
    title = models.CharField(max_length=200) #제한된 텍스트 정의
    text = models.TextField() #제한없는 텍스트 정의
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
