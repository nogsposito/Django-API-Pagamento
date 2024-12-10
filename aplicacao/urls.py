from django.urls import path
from . import views

app_name = 'aplicacao'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('compra_efetuada/', views.CompraEfetuadaView.as_view(), name='compra_efetuada'),
    path('compra_erro/', views.CompraErroView.as_view(), name='compra_erro'),
]