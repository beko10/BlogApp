from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm
from .forms import LoginForm
from .forms import ProfileDeleteForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from article .models import Article
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def register(request):

    #request çeşidine göre form oluştu request.Post ise post requesttir formdan gelen bilgiler alındı None ise form boş get requesttir  
    form = RegisterForm(request.POST or None)
    #formdaki bilgiler kontrol edildi 
    if form.is_valid():
        #fromdan gelen bilgiler alındı 
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        #kayıt olacak kullanıcı için User sınıfından yeni bi obje oluşturuldu ve bu objenin özelliklerine formdan gelen bilgiler atandı 
        newUser = User(username=username)
        newUser.set_password(password)
        #kullanıcı veri tabanına kayıt edildi 
        newUser.save()
        #kullanıcı girişi yapıldı 
        login(request,newUser)

        messages.success(request,"Kayıt Başarılı...")

        return redirect("index")

    #request none ise oluşturulan form gösterilir     
    contex = {
        "form":form
    }

    return render(request,"register.html",contex)



"""
    KULLANICI KAYIT-1
    if request.method == "POST":
         #request.POST metodu ile forma girilen bilgilen alındı bu bilgiler form objesine atandı 
        form = RegisterForm(request.POST)
        #is_valid() metodu forms.py dosyasının içindeki clean metodunu çağırır eğer clean metodunu overriding yaparak baktığımız password ile confirm alanı aynı ise is_valid metodu
        #true döndürür değilse false 
        if form.is_valid():
            #clean metodundaki alınan veriler key degerlerine göre tekrar alındı 
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            #alınan bilgiler ile User modeli kullanılarak yeni bir kullanıcı formdan alınan bilgiler oluşturuldu
          
            #Alternatif kullanıcı oluşturma
            #newUser = User()
            #newUser.username = username
            #newUser.set_password(password)
              
              
              

            newUser = User(username=username)
            newUser.set_password(password)
            #oluşturulan kullanıcı veri tabanına kayıt edildi 
            newUser.save()
            #kayıt olan kullanıcı siteye giriş yaptı 
            login(request,newUser)



            
            
            #Alternatif başka url yönlendirme 
            #target_url = "index"
            #return redirect(target_url)

            #return redirect(target_url)
            #target_url = reverse("index")
            #return redirect(target_url)
            return redirect(target_url)
            
           
            #Kullanıcıyı belirlediğiniz URL'ye yönlendirin.
            
            return redirect("index")


        #Porlalar yanlış ise 
        context = {
        "form":form
        } 
        return render(request,"register.html",context)
     
    else:
        #boş form oluşturuldu 
        form = RegisterForm()
        #form içeriğinin ön uca göndermek için contex sözlüğü oluşturuldu bu sozlukteki belirlenen key ile ön uçta gönderilen form bilgisine nasıl ulaçıcağı belirlendi
        context = {
        "form":form
        } 
    return render(request,"register.html",context)
    """
  




    
def loginUser(request):
    #requeste göre fom oluşturuldu 
    form = LoginForm(request.POST or None)
    contex = {
        "form":form
    }
    #form kontrolü yapıldı
    if form.is_valid():
        #formdaki bilgiler alındı 
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        #formdaki bilgiler ile veri tabanındaki bilgiler var mı kontrol edildi 
        #authenticate metodu aldığı username ve password bilgisine göre veri tabanında kullanıcının olup olmadığını bulur kullanıcı varsa kullanıcının bilgisini döner yoksada None döner
        user = authenticate(request, username=username, password=password)
        #kullanıcın girdiği bilgiler veri tabanındaki bilgiler ile uyuşmuyorsa
        if user is None:
            messages.error(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",contex)
        #kullanıcının girdiği bilgiler uyuşuyorsa     
        else:
            messages.success(request,"Giriş Başarılı...")
            login(request,user)
            return redirect("index")
    return render(request,"login.html",contex)









"""
       if user is not None:
            login(request, user)
            messages.success(request,"Giriş Başarılı")
            return redirect("index")
        else:
            messages.error(request,"Şifre veya kullanıcı adı hatalı")
            return render(request,"login.html",contex)    
    else:
        return render(request,"login.html",contex)



""" 
    

    
def logoutUser(request):
    #request bilgisine göre kullanıcın oturumu kapatıldı 
    logout(request)
    messages.success(request,"Çıkış Yapıldı")
    return redirect("index")




@login_required
def profile(request,id):

    usercontrol = get_object_or_404(User,pk=id)
    article_count = Article.objects.filter(author=usercontrol).count()
    return render(request,"profile.html",{"article_count":article_count})


@login_required
def ProfileDelete(request,id):
    #kullanıcı veri tabanından sogulandı eğer boyle bi kullanıcı yoksa 404 hatası dönexek
    user = get_object_or_404(User,pk=id)
    #ProfileDeleteForm sınıfından requeste göre form oluşturuldu 
    form = ProfileDeleteForm(request.POST or None)
    contex = {
        "form":form
    }
    #form bilgileri kontrol edildi     
    if form.is_valid():
        #formdan gelen bilgiler alındı 
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        #formdaki bilgiler ile veri tabanındaki bilgiler kıyaslandı eğer uyuşuyorsa 
        if user.username == username and user.check_password(password):
            #kullanıcının oturumu kapatıldı 
            logout(request)
            messages.success(request,"profiliniz silindi")
            #kullanıcıya ait veriler veri tabanından silindi 
            user.delete()
            return redirect("index")
        #formdaki bilgiler uyuşmuyorsa
        else:
            messages.error(request,"kullanıcı adı veya parola yanlış")
            return render(request,"profiledelete.html",contex)

   
    return render(request,"profiledelete.html",contex)






"""

def ProfileDelete(request, id):
    form = ProfileDeleteForm(request.POST or None)
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        try:
            user = User.objects.get(pk=id)
            
            if username == user.username and user.check_password(password):
                logout(request)
                messages.success(request, "Profiliniz başarıyla silindi.")
                user.delete()
                return redirect("index")
            else:
                messages.error(request, "Kullanıcı adı veya parola hatalı.")
        
        except User.DoesNotExist:
            messages.error(request, "Kullanıcı bulunamadı.")
    
    form = {
        "form": form
    }
    
    return render(request, "profiledelete.html", form)









"""
"""
NOT: Kullanıcı Kayıt yontemi - 1 clean metodunu overridding ederek clean metodunun nasıl çalışacağınız biz belirledik ve is_valid metodu buna göre true ya da false değer

döndürekcek ancak Kullanıcı Kayıt yontemi - 2 clean metodunu overriding etmedik clean metodu default olarak çalışacak ve is_valid metodu fomdaki alanlara belirtildiği gibi 

doldurursa true değilse false dödürecektir 

"""    