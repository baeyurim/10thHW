from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

#제목,본문, 날짜, 그림
class Diary(models.Model):
    title=models.CharField(max_length=50)
    body=models.TextField(null=False)
    image=models.ImageField(upload_to='images/')
    date=models.DateTimeField('date published', default = timezone.datetime.now())
    writer=models.CharField(max_length=50, default = "default")
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(80, 80)])
    def sum(self):
        return self.body[:20]

class Comment(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, null = True, related_name='comments')
    contents = models.CharField(max_length=500)
    com_writer=models.CharField(max_length=50, default = "default")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.contensts
