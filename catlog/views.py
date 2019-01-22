from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Catlog_images, Food, Accessories, Art, Backgrounds, Beauty, Business, Celebrate, Children, Cinema, City, Communication, Education, Fashion, Fitness, Flowers, Health, Holidays, Home, Jewlery, Landscape, Love, Money, Nature, People, Recreation, Retail, Seasons, Spring, Technology, Transportation, Travel, Urbanlife, Wellness, Work, World
# Create your views here.


def catlog_home(request):
    catlog_image_url = Catlog_images.objects.order_by('-id')

    context = {
        'catlog_image_url': catlog_image_url,
    }
    return render(request, 'catlog/catlog_home.html', context)


def food(request):
    food_url = Food.objects.order_by('-id')
    paginator = Paginator(food_url, 44)
    page = request.GET.get('page')
    food_url = paginator.get_page(page)
    context = {
        'food_url': food_url,
    }
    return render(request, 'catlog/food.html', context)


def accessories(request):
    accessories_url = Accessories.objects.order_by('-id')
    paginator = Paginator(accessories_url, 44)
    page = request.GET.get('page')
    accessories_url = paginator.get_page(page)
    context = {
        'accessories_url': accessories_url,
    }
    return render(request, 'catlog/accessories.html', context)


def art(request):
    art_url = Art.objects.order_by('-id')
    paginator = Paginator(art_url, 44)
    page = request.GET.get('page')
    art_url = paginator.get_page(page)
    context = {
        'art_url': art_url,
    }
    return render(request, 'catlog/art.html', context)


def backgrounds(request):
    backgrounds_url = Backgrounds.objects.order_by('-id')
    paginator = Paginator(backgrounds_url, 44)
    page = request.GET.get('page')
    backgrounds_url = paginator.get_page(page)
    context = {
        'backgrounds_url': backgrounds_url,
    }
    return render(request, 'catlog/backgrounds.html', context)


def beauty(request):
    beauty_url = Beauty.objects.order_by('-id')
    paginator = Paginator(beauty_url, 44)
    page = request.GET.get('page')
    beauty_url = paginator.get_page(page)
    context = {
        'beauty_url': beauty_url,
    }
    return render(request, 'catlog/beauty.html', context)


def business(request):
    business_url = Business.objects.order_by('-id')
    paginator = Paginator(business_url, 44)
    page = request.GET.get('page')
    business_url = paginator.get_page(page)
    context = {
        'business_url': business_url,
    }
    return render(request, 'catlog/business.html', context)


def celebrate(request):
    celebrate_url = Celebrate.objects.order_by('-id')
    paginator = Paginator(celebrate_url, 44)
    page = request.GET.get('page')
    celebrate_url = paginator.get_page(page)
    context = {
        'celebrate_url': celebrate_url,
    }
    return render(request, 'catlog/celebrate.html', context)


def children(request):
    children_url = Children.objects.order_by('-id')
    paginator = Paginator(children_url, 44)
    page = request.GET.get('page')
    children_url = paginator.get_page(page)
    context = {
        'children_url': children_url,
    }
    return render(request, 'catlog/children.html', context)


def cinema(request):
    cinema_url = Cinema.objects.order_by('-id')
    paginator = Paginator(cinema_url, 44)
    page = request.GET.get('page')
    cinema_url = paginator.get_page(page)
    context = {
        'cinema_url': cinema_url,
    }
    return render(request, 'catlog/cinema.html', context)


def city(request):
    city_url = City.objects.order_by('-id')
    paginator = Paginator(city_url, 44)
    page = request.GET.get('page')
    city_url = paginator.get_page(page)
    context = {
        'city_url': city_url,
    }
    return render(request, 'catlog/city.html', context)


def communication(request):
    communication_url = Communication.objects.order_by('-id')
    paginator = Paginator(communication_url, 44)
    page = request.GET.get('page')
    communication_url = paginator.get_page(page)
    context = {
        'communication_url': communication_url,
    }
    return render(request, 'catlog/communication.html', context)


def education(request):
    education_url = Education.objects.order_by('-id')
    paginator = Paginator(education_url, 44)
    page = request.GET.get('page')
    education_url = paginator.get_page(page)
    context = {
        'education_url': education_url,
    }
    return render(request, 'catlog/education.html', context)


def fashion(request):
    fashion_url = Fashion.objects.order_by('-id')
    paginator = Paginator(fashion_url, 44)
    page = request.GET.get('page')
    fashion_url = paginator.get_page(page)
    context = {
        'fashion_url': fashion_url,
    }
    return render(request, 'catlog/fashion.html', context)


def fitness(request):
    fitness_url = Fitness.objects.order_by('-id')
    paginator = Paginator(fitness_url, 44)
    page = request.GET.get('page')
    fitness_url = paginator.get_page(page)
    context = {
        'fitness_url': fitness_url,
    }
    return render(request, 'catlog/fitness.html', context)


def flowers(request):
    flowers_url = Flowers.objects.order_by('-id')
    paginator = Paginator(flowers_url, 44)
    page = request.GET.get('page')
    flowers_url = paginator.get_page(page)
    context = {
        'flowers_url': flowers_url,
    }
    return render(request, 'catlog/flowers.html', context)


def health(request):
    health_url = Health.objects.order_by('-id')
    paginator = Paginator(health_url, 44)
    page = request.GET.get('page')
    health_url = paginator.get_page(page)
    context = {
        'health_url': health_url,
    }
    return render(request, 'catlog/health.html', context)


def holidays(request):
    holidays_url = Holidays.objects.order_by('-id')
    paginator = Paginator(holidays_url, 44)
    page = request.GET.get('page')
    holidays_url = paginator.get_page(page)
    context = {
        'holidays_url': holidays_url,
    }
    return render(request, 'catlog/holidays.html', context)


def home(request):
    home_url = Home.objects.order_by('-id')
    paginator = Paginator(home_url, 44)
    page = request.GET.get('page')
    home_url = paginator.get_page(page)
    context = {
        'home_url': home_url,
    }
    return render(request, 'catlog/home.html', context)


def jewlery(request):
    jewlery_url = Jewlery.objects.order_by('-id')
    paginator = Paginator(jewlery_url, 44)
    page = request.GET.get('page')
    jewlery_url = paginator.get_page(page)
    context = {
        'jewlery_url': jewlery_url,
    }
    return render(request, 'catlog/jewlery.html', context)


def landscape(request):
    landscape_url = Landscape.objects.order_by('-id')
    paginator = Paginator(landscape_url, 44)
    page = request.GET.get('page')
    landscape_url = paginator.get_page(page)
    context = {
        'landscape_url': landscape_url,
    }
    return render(request, 'catlog/landscape.html', context)


def love(request):
    love_url = Love.objects.order_by('-id')
    paginator = Paginator(love_url, 44)
    page = request.GET.get('page')
    love_url = paginator.get_page(page)
    context = {
        'love_url': love_url,
    }
    return render(request, 'catlog/love.html', context)


def money(request):
    money_url = Money.objects.order_by('-id')
    paginator = Paginator(money_url, 44)
    page = request.GET.get('page')
    money_url = paginator.get_page(page)
    context = {
        'money_url': money_url,
    }
    return render(request, 'catlog/money.html', context)


def nature(request):
    nature_url = Nature.objects.order_by('-id')
    paginator = Paginator(nature_url, 44)
    page = request.GET.get('page')
    nature_url = paginator.get_page(page)
    context = {
        'nature_url': nature_url,
    }
    return render(request, 'catlog/nature.html', context)


def people(request):
    people_url = People.objects.order_by('-id')
    paginator = Paginator(people_url, 44)
    page = request.GET.get('page')
    people_url = paginator.get_page(page)
    context = {
        'people_url': people_url,
    }
    return render(request, 'catlog/people.html', context)


def recreation(request):
    recreation_url = Recreation.objects.order_by('-id')
    paginator = Paginator(recreation_url, 44)
    page = request.GET.get('page')
    recreation_url = paginator.get_page(page)
    context = {
        'recreation_url': recreation_url,
    }
    return render(request, 'catlog/recreation.html', context)


def retail(request):
    retail_url = Retail.objects.order_by('-id')
    paginator = Paginator(retail_url, 44)
    page = request.GET.get('page')
    retail_url = paginator.get_page(page)
    context = {
        'retail_url': retail_url,
    }
    return render(request, 'catlog/retail.html', context)


def seasons(request):
    seasons_url = Seasons.objects.order_by('-id')
    paginator = Paginator(seasons_url, 44)
    page = request.GET.get('page')
    seasons_url = paginator.get_page(page)
    context = {
        'seasons_url': seasons_url,
    }
    return render(request, 'catlog/seasons.html', context)


def spring(request):
    spring_url = Spring.objects.order_by('-id')
    paginator = Paginator(spring_url, 44)
    page = request.GET.get('page')
    spring_url = paginator.get_page(page)
    context = {
        'spring_url': spring_url,
    }
    return render(request, 'catlog/spring.html', context)


def technology(request):
    technology_url = Technology.objects.order_by('-id')
    paginator = Paginator(technology_url, 44)
    page = request.GET.get('page')
    technology_url = paginator.get_page(page)
    context = {
        'technology_url': technology_url,
    }
    return render(request, 'catlog/technology.html', context)


def transportation(request):
    transportation_url = Transportation.objects.order_by('-id')
    paginator = Paginator(transportation_url, 44)
    page = request.GET.get('page')
    transportation_url = paginator.get_page(page)
    context = {
        'transportation_url': transportation_url,
    }
    return render(request, 'catlog/transportation.html', context)


def travel(request):
    travel_url = Travel.objects.order_by('-id')
    paginator = Paginator(travel_url, 44)
    page = request.GET.get('page')
    travel_url = paginator.get_page(page)
    context = {
        'travel_url': travel_url,
    }
    return render(request, 'catlog/travel.html', context)


def urbanlife(request):
    urbanlife_url = Urbanlife.objects.order_by('-id')
    paginator = Paginator(urbanlife_url, 44)
    page = request.GET.get('page')
    urbanlife_url = paginator.get_page(page)
    context = {
        'urbanlife_url': urbanlife_url,
    }
    return render(request, 'catlog/urbanlife.html', context)


def wellness(request):
    wellness_url = Wellness.objects.order_by('-id')
    paginator = Paginator(wellness_url, 44)
    page = request.GET.get('page')
    wellness_url = paginator.get_page(page)
    context = {
        'wellness_url': wellness_url,
    }
    return render(request, 'catlog/wellness.html', context)


def work(request):
    work_url = Work.objects.order_by('-id')
    paginator = Paginator(work_url, 44)
    page = request.GET.get('page')
    work_url = paginator.get_page(page)
    context = {
        'work_url': work_url,
    }
    return render(request, 'catlog/work.html', context)


def world(request):
    world_url = World.objects.order_by('-id')
    paginator = Paginator(world_url, 44)
    page = request.GET.get('page')
    world_url = paginator.get_page(page)
    context = {
        'world_url': world_url,
    }
    return render(request, 'catlog/world.html', context)
