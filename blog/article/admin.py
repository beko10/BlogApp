from django.contrib import admin

from .models import Article
# Register your models here.

"""
admin.py Dosyası 
------------------
Django admin panelini özelleştirmek ve modelleri(veritabanı tablolarını) kayıt etmek için kullanılır

"""
#Modelleri Kayıt Etme Yontemi - 1
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #admin panelinde makeleler ile ilgili gösterilecek özellikler belirlendi
    list_display = ["title","author","created_date"]

    #admin panelinde makalelerin gösterilen özelliklerine link özelliği verildi 
    list_display_links = ["title","created_date"]

    #admin panelinde makalelerin title bilgisine göre arama özelliği eklendi 
    search_fields = ["title"]

    #admin panelinde makalelerin oluşturulma tarihlerine göre filtre eklendi.Bu makalelerin(model) diğer özelliklerine göre de yapılabilirdi
    list_filter = ["created_date"]
    #Article ile admin.ModelAdmin arasında bağlantı kuracak sınıf 
    class Meta:
        #Article ile admin.ModelAdmin bağlantı kuruldu ve decorators metod yardımı ile Article tablomuz bağlantı sayesinde kayıt edildi
        model = Article

# Modelleri Kayıt Etme Yontemi - 2
# admin.site.register(MyModel)