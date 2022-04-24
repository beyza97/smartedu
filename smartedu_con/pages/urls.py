# 6.ADIM PAGES/URLS OLUŞTURULUR VE 3. 4. İŞLEMLER BURAYA TAŞINIR
from django.urls import path
from pages import views 
# artık pages altında bir klasörde olduğu için oages yerine . kullanılır

urlpatterns = [
    path('', views.index), 

]
# BU URL İŞLEMLERİ ANA URLS OLAN SMARTEDU/URLS.PY' DE TANITILMALIDIR.