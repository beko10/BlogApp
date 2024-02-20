from django.db import models

class Comment(models.Model):
    article = models.ForeignKey('article.Article', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50,verbose_name="isim")
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return self.comment