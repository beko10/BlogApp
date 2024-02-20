from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
from comment.models import Comment
from comment.forms import CommentForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def index(request):

    contex = {
        "sayi":10 
   }
   
    return render(request,"index.html",contex)

def about(request):
    return render(request,"about.html")


def arama(request):
    # Arama sorgusu işlemleri burada gerçekleştirilir
    if request.method == "POST":
        query = request.POST.get('keyword')
        sonuclar = []
        if query:
            #User tablosundaki bilgiler post requesten alınan bilgiler yukarıdaki query listesinin içine bakılarak eşleşen öğeler sonuclar listesine alındı  
            sonuclar = User.objects.filter(username__icontains=query)
            print(sonuclar)
            return render(request, 'arama.html', {'sonuclar': sonuclar, 'query': query})        
        # Arama sorgusu ile ilgili veritabanı veya başka bir kaynak üzerinden sonuçları alın

    return redirect("index")

















def comment(request,id):
    #yorum yapılacak makale veri tabanında var mı diye bakıldı yoksa 404 sayfası döndürülecek
    article = get_object_or_404(Article, pk=id)
    #yorum formu oluşturuldu requestine göre
    form = CommentForm(request.POST or None)
    #formdaki bilgiler kontrol edildi
    if form.is_valid():
        #formdan gelen bilgiler alındı 
        author = form.cleaned_data.get("author")
        comment = form.cleaned_data.get("comment")
        #Comment sınıfından obje oluşturuldu ve formdan gelen bilgiler oluşturulan objenin ilgili özelliklerine atandı 
        newComment = Comment(author=author,comment=comment)
        #Comment sınıfından oluşturulan objenin article özelliğine alınan article atandı yani yorumla article bağlandı 
        newComment.article = article
        #yorum veri tabanına kayıt edildi 
        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))









"""
def comment(request, id):
    # Yorum yapılacak makaleyi alın
    article = get_object_or_404(Article, pk=id)

    # Yorum formunu oluşturun
    form = CommentForm(request.POST or None)

    if form.is_valid():
        # Formdan gelen bilgilerle yorum oluşturun ve makaleye bağlayın
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect("index")
    
    context = {
        "form": form,
        "article": article,
    }
    
    return render(request, "articles.html", context)


"""


def articlesView(request):

    articles = Article.objects.all()
    comments = Comment.objects.filter(article__in=articles)
    return render(request,"articles.html",{"articles":articles,"comments":comments})


@login_required(login_url="user:login")
def dashboard(request):
    #kullanıcın yazdığı makaleler veri tabanından alındı
    articles = Article.objects.filter(author=request.user)
    #alınan makalelerin ön uca gönderilecek ön uçta"articles"
    contex = {
        "articles":articles
    }
    return render(request,"dashboard.html",contex)
 
@login_required(login_url="user:login")
def addArticles(request):
    form = ArticleForm(request.POST  or None,request.FILES or None)
  
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başrıyla Olulşturuldu")
        return redirect("index")
    
    form = {
        "form":form
    }
    return render(request,"addarticles.html",form)  
    




"""   
def addArticles(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # Yazarı mevcut oturum açmış kullanıcı olarak belirle
            article = form.save(commit=False)
            article.author = request.user  # Bu satırı ekleyin
            article.save()
            return redirect('index')
    else:
        form = ArticleForm()
    
    return render(request, "addarticles.html", {"form": form})
""" 


def arama(request):
    #"keyword"anahtar kelimesi ile ön uçta navbarda aranan harfleri aldık
    query = request.POST.get("keyword")
    sonuclar = []
    if query:
        #article tablosunda title bilgisinde bulunan harfler query içerisinde arandı 
        sonuclar = Article.objects.filter(title__icontains=query)

    return render(request,"arama.html",{"sonuclar":sonuclar,"query":query})







@login_required(login_url="user:login")
def detail(request,id):
    
    

    article = get_object_or_404(Article,pk=id)

    comments = article.comments.all()

    return render(request,"detail.html",{"article":article,"comments":comments})
#kullanıcı giriş yapmadan get request ile sayfaya gitmesi engellenir giderse login sayfasına yönlendirilir
@login_required(login_url="user:login")
def Articleupdate(request,id):
    article = Article.objects.get(id=id)
    #instance parametresi ile formu atricle objesinin bilgileriile başlatıldı ve form adında  AricleFormdan obje oluşturuldu  
    form = ArticleForm(request.POST  or None,request.FILES or None,instance=article)

    if form.is_valid(): 
        #fromdan gelen bilgilerle article objesi oluşturuldu 
        article = form.save(commit=False)
        #requesten gelen bilgi modelde bulunan article.author bilgisine atandı yani makale ilgili kullanıcıya bağlandı 
        article.author = request.user
        #guncellenen makale veri tabanına kayıt edildi 
        article.save()
        messages.success(request,"Makale Başarılı Bir Şekilde Guncellendi")
        return redirect("index")
    form = {
        "form":form
    }
    return render(request,"articleupdate.html",form)
    
@login_required(login_url="user:login")    
def Articledelete(request,id):
    #makale yokse 404 sayfası döner
    artricle = get_object_or_404(Article,pk=id)
    messages.error(request,"Makale Silindi...")
    #makale veri tabanından silinir
    artricle.delete()
    return render(request,"index.html")



