from django.db import models
from django.utils import timezone

# Create your models here.
class Answer(models.Model):
    answer = models.CharField('答え', max_length= 30)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    likes = models.IntegerField(null=True, blank=True, default=0)


    def __str__(self):
        return self.answer


class Question(models.Model):
    title = models.CharField('タイトル', max_length=50)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    answer = models.ForeignKey(Answer, verbose_name='答え', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField('お名前', max_length=50)
    text = models.TextField('コメント')
    answer = models.ForeignKey(Answer, verbose_name='紐づく答え', on_delete=models.PROTECT)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.text