from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'pages'

urlpatterns =[
    path('', views.index, name='index' ),
    path('help/', views.help, name='help' ),
    path('calculadora/', views.calculadora, name='calculadora' ),
    path('londrina/', views.londrina, name='londrina' ),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)