from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm


def news_home(request):
    news = Artiles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    error = ''


    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма было не верно'
    form = ArtilesForm()

    data = {
        'form': form
    }
    
    return render(request, 'news/create.html', data)