from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('dnsCreator', views.dnsCreator, name = 'dnsCreator'),
    path('RandomWords', views.RandomWords, name = 'RandomWords'),
    path('HeaderDecoder', views.HeaderDecoder, name = 'HeaderDecoder'),
    path('dnsCheck', views.dnsCheck, name = 'dnsCheck'),
    path('ReverseCheck', views.ReverseCheck, name = 'ReverseCheck'),
    path('DnsBl', views.DnsBl, name = 'DnsBl'),
    path('IpClassConverter', views.IpClassConverter, name = 'IpClassConverter'),
    path('dnsGenerator', views.dnsGenerator, name = 'dnsGenerator'),
    path('RandomWordsGenerator', views.RandomWordsGenerator, name = 'RandomWordsGenerator'),
    path('HeaderDecoderGenerator', views.HeaderDecoderGenerator, name = 'HeaderDecoderGenerator'),
    path('ReverseGenerator', views.ReverseGenerator, name = 'ReverseGenerator'),
    path('DnsBlGenerator', views.DnsBlGenerator, name = 'DnsBlGenerator'),
    path('IpClassGenerator', views.IpClassGenerator, name = 'IpClassGenerator'),
    path('dnsChecker', views.dnsChecker, name = 'dnsChecker')
]
