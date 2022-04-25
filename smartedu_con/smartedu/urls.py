"""smartedu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #7.ADIM INCLUDE EKLENDİ 
# 4. ADIM # 
# from pages import views #pages uygulamasında yer alan views buraya tanıtılır ve path('', pages.views.index) yerine path('',views.index) yazılabilir.
#böylece hata sonlanır

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')), #7. ADIM INCLUDE KULLANILDI VE PAGES UYGULAMASI URLS DOSYASI BURAYA TANITILDI
    # 3. ADIM #
#    path('', views.index), # sayfa adresine hiçbir ekleme yapılmadan (127.0.0.1:8000 haline) girilirse pages
    # uygulamasındaki views.py de yer alan index fonksiyonunu çağır. şu an PAGES IS NOT DEFINED hatası geliyor.

]

 # 5. ADIM --- ADRESLEME ANA UYGULAMA URLS'İ YERİNE KULLANILACAĞI UYGULAMA İÇERİSİNE BİR URLS AÇILIP ORADA YÖNETİLİR.
 # YANİ 3. VE 4. ADIMLARIN UYGULANACAĞI YER DEĞİŞTİĞİ İÇİN IMPORT VE PATH SATIRLARI COMMENTE ALINDI 