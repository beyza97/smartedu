from django.shortcuts import render
#################
# İLK BAŞLANGIÇ #
#################

# 1. ADIM #
from django.http import HttpResponse #ilgili isteklere(requestler)  cevap(response) dönmesi için import edildi

# 2. ADIM #
def index(request):
    
    return HttpResponse("<h1>INDEX SAYFASI</h1>")
#index fonksiyonu requesti alır ve bu isteğe karşılır bir http response döner ve Index sayfası yazısı çıkar.
#bu aşamadan sonra ; smartedu/urls.py klasörüne girilir urlpatterns=[] içerisine bir path daha eklenir.

# 3. ADIM İÇİN ---> SMARTEDU/URLS.PY KLASÖRÜNE GİDİLİR. 