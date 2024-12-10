from django.shortcuts import render
from django.views import View

class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')
    
class CompraEfetuadaView(View):

    def get(self, request):
        return render(request, 'compra_efetuada.html')
    
class CompraErroView(View):

    def get(self, request):
        return render(request, 'compra_erro.html')