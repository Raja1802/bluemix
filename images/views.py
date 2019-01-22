from django.shortcuts import render
from .models import Set_1,High_resolve_urls
from django.core.paginator import Paginator
from django.http import HttpResponse
# Create your views here.


def index(request):
    data = Set_1.objects.order_by('-id')
    top_image = High_resolve_urls.objects.get(id=29)
    paginator = Paginator(data, 24)
    page = request.GET.get('page')
    data = paginator.get_page(page)
    context = {
        'data': data,
        'top_image': top_image,
    }
    return render(request, 'images/index.html', context)


def all_images(request):
    data = Set_1.objects.order_by('-id')
    paginator = Paginator(data, 44)
    page = request.GET.get('page')
    data = paginator.get_page(page)
    context = {
        'data': data,
    }
    return render(request, 'images/all_images.html', context)
