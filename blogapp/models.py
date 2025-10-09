from django.db import models

class BlogPost(models.Model):

    CATEGORY = (('science', '科学のこと'),
                ('dailylife', '日常のこと'),
                ('music', '音楽のこと'))
    
    #タイトル用
    title = models.CharField(
        verbose_name= 'タイトル',
        max_length=200
        )
    
    #本文
    content = models.TextField(
        verbose_name='本文'
        )
    
    #投稿日時
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
        )
    
    #カテゴリ
    category = models.CharField(
        verbose_name='カテゴリ',
        max_length=20,
        choices=CATEGORY
        )
    
    def __str__(self):
        return self.title
