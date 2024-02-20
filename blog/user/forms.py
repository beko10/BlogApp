from django import forms
from django.contrib.auth.models import User
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanici Adi")
    password = forms.CharField(max_length=20,label="Parola",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label="Parola Doğrula",widget=forms.PasswordInput)

    #clean metodu ile formdaki bilgiler submit edilmeden önce bilgileri kontrol ettik NOT:Burda clean metodunu Override ettik 
    def clean(self):
        #formdaki bilgiler alındı 
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        #password ve confirm alanı dolduruldu mu ve password alanındaki veri confirm alanındaki veri farklıysa
        if password and confirm and password != confirm:
            raise forms.ValidationError("parolalar eşleşmiyor")
        

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("bu kullanıcı adı zaten kullanılıyor")
        #if koşulu sağlanmaz ise yani formdaki herşey doğru ise clean metodu values sözlüğünü dödürür
        values = {
            "username" : username,
            "password" : password,
            
        }
        return values

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanici Adi")
    password = forms.CharField(max_length=20,label="Parola",widget=forms.PasswordInput)

class ProfileDeleteForm(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanici Adi")
    password = forms.CharField(max_length=20,label="Parola",widget=forms.PasswordInput)





"""
NOT:
Django'da clean metodu, bir formun verilerini doğrulamak, temizlemek ve özelleştirmek için kullanılan önemli bir metottur. clean metodu, Django form nesnelerinin bir parçasıdır ve genellikle alt sınıflarda özelleştirilir.

clean metodunun temel görevleri şunlar içerir:

Veri Doğrulama (Validation): clean metodu, form alanlarından gelen verileri belirli kurallara göre doğrular. Örneğin, bir alanın boş olmaması, belirli bir veri türünü içermesi veya özel bir koşulu karşılaması gerekebilir. Veri doğrulaması sırasında hatalı veriler tespit edilir ve hata mesajları oluşturulabilir.

Temizleme (Cleaning): clean metodu, gelen verileri işleyerek, istenen veri formatına dönüştürebilir veya gerektiğinde temizleyebilir. Örneğin, kullanıcı tarafından girilen metni belirli bir biçime dönüştürmek veya veriyi uygun bir şekilde düzenlemek.

Özel İşlemler (Custom Processing): clean metodu, form alanlarından gelen veriler üzerinde özel işlemler gerçekleştirmenizi sağlar. Bu, belirli koşullara bağlı olarak bazı alanları otomatik olarak doldurmak veya verilere eklemeler yapmak gibi işlemleri içerebilir.

Özellikle, clean metodunu kullanarak veri doğrulama ve temizleme işlemlerini yapabilir ve form verilerini uygun bir şekilde işleyebilirsiniz. Bu, kullanıcıların formu doğru şekilde doldurmalarını sağlamak ve hatalı verileri işlemek için önemlidir. Form verilerinin işlenmiş ve doğrulanmış olduğundan emin olmak, güvenli ve tutarlı verilerin kullanılmasını sağlar.

"""