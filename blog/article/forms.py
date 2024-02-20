from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    #ArticleForm ile forms.ModelForm arasındaki bağlantıyı kuracak sınıf
    class Meta:
        #Aradaki bağlantı kuruldu 
        model = Article
        #form da olacak alanlar belirlendi 
        fields = ["title","content","article_image"]