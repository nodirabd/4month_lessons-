from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse #одинарное сообщение
from .import models

def blog_detail_view(request, id):
    if request.method == 'GET':
        blog_id = get_object_or_404(models.Blog, id=id) #получаем объект модели Blog по id
        return render(request, 'blog_detail.html', {'blog': blog_id}) #передаем объект модели Blog в шаблон blog_detail.html

def blog_list_view(request):
    if request.method == 'GET': #проверяем метод запроса
        query_blog = models.Blog.objects.all().order_by('-id') #получаем все объекты модели Blog
        return render(request, 'blog_list.html', {'blogs': query_blog}) 
    


def message(request):
    return HttpResponse('Это мой первый проект на джанго')
