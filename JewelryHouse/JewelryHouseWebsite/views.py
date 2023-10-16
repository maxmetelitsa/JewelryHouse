from django.shortcuts import render

def index_page(request):
    return render(request, 'index.html')

def jewelryMarket_page(request):
    return render(request, 'jewelryMarket.html')

def news_page(request):
    return render(request, 'news.html')

def stockists_page(request):
    return render(request, 'stockists.html')

def about_page(request):
    return render(request, 'about.html')
