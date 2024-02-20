from django.contrib import admin
from django.urls import path

from article  import views

app_name = "article"

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addarticles/',views.addArticles,name="addarticles"),
    path('article/<int:id>',views.detail,name="detail"),
    path('update/<int:id>',views.Articleupdate,name="update"),
    path('delete/<int:id>',views.Articledelete,name="delete"),
    path('comment/<int:id>',views.comment,name="comment"),
    path('',views.articlesView,name="articlesView"),
    
]



