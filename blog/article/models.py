from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings

# Create your models here.

"""
models.py Dosyası
-------------------
Veri tabanı tablolarını özelliklerinini(veri modülleri) tanımlayan ve yöneten dosyadır.Bu dosyada veri tabanında bulunan verilerin ORM ile birbirleriyle olan ilişkileri tanımlanır


"""

#Article tablosu oluşturuldu 
class Article(models.Model):
    #Aricle tablosundaki verilerin özellikleri ve ilişkileri bvelirlendi 
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title = models.CharField(max_length=80,verbose_name="Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(blank=True, null=True, verbose_name="Makaleye Fotoğraf Ekle")
    #admin panelinde makalelerin nasıl görüneceği ayarlandı 
    def __str__(self):
        return self.title
