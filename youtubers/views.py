from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Youtuber
# Create your views here.


def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_at')
    data = {
        'tubers': tubers
    }
    return render(request, 'youtubers/youtubers.html', data)


def youtubers_detail(request, id):
    tuber = get_object_or_404(Youtuber, pk=id)
    data = {
        "tuber": tuber
    }
    return render(request, 'youtubers/youtuber_detail.html', data)


def search(request):
    tubers = Youtuber.objects.order_by('-created_at')
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_search = Youtuber.objects.values_list(
        'camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list(
        'category', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(Q(description__icontains=keyword) | Q(
                first_name__icontains=keyword) | Q(last_name__icontains=keyword))

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(Q(city__iexact=city))

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(Q(camera_type__iexact=camera_type))

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(Q(category__iexact=category))

    data = {
        'tubers': tubers,
        'city_search': city_search,
        'camera_search': camera_search,
        'category_search': category_search,
    }
    return render(request, 'youtubers/search.html', data)
