from django.apps import AppConfig

"""
apps.py Dosyası 
----------------
Uygulamanın yapılandırma ayarlarını içeren dosyadır


"""

class ArticleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'article'
