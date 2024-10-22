from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .models import Image, Service, Gallery, Information, Review
from .forms import ReviewModelForm, CallForm
import requests
from django.utils.timezone import now
from django.contrib import messages

# Create your views here.
def main(request):
    images = Image.objects.filter(gallery__title='Главная')
    images2 = Image.objects.filter(gallery__title='Наши последние работы')
    if request.method == 'POST' and "Call" in request.POST and not request.COOKIES.get('timer'):
        form = CallForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            number = form.cleaned_data['number']
            hour = form.cleaned_data['hour']
            minute = form.cleaned_data['minute']
            comment = form.cleaned_data['comment']
            
            email_message = f'Имя: {name}.\nНомер телефона: {number}.\nУдобное время: {hour}:{minute}.\nКомментарий: "{comment}".'

            send_mail(
                'Запрос на звонок',
                email_message,
                'starzev.kolechka@gmail.com',  # От кого
                ['maximagapitow@gmail.com'],  # Кому
                fail_silently=False,
            )
            cookie_lifetime = 3600
            current_time = now()
            response = redirect('/')
            response.set_cookie('timer', current_time, max_age=cookie_lifetime)
            return response
    else:
        form = CallForm()
   
    return render(request, "main.html", {'images': images, 'images2': images2})

def service(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'service.html', {'service': service})

def services(request):
    return render(request, "services.html")

def information(request, slug):
    information = get_object_or_404(Information, slug=slug)
    return render(request, 'information.html', {'information': information})

def informations(request):
    return render(request, 'informations.html')

def gallery(request, slug):
    gallery = get_object_or_404(Gallery, slug=slug)
    images = Image.objects.filter(gallery__slug=gallery.slug)
    return render(request, "gallery.html", {'gallery': gallery, 'images': images})

def gallerys(request):
    return render(request, 'gallerys.html')

def aboutUs(request):
    images = Image.objects.filter(gallery__title='О нас')
    return render(request, "aboutUs.html", {'images': images})

def reviews(request):
    if request.method == "POST" and not request.COOKIES.get('review_submitted'):
        form = ReviewModelForm(request.POST)
        if form.is_valid():
            form.save()
            response = redirect('/reviews')
            response.set_cookie('review_submitted', 'true', max_age=365*24*60*60)
            return response
    else:
        form = ReviewModelForm()

    reviews = Review.objects.all()
    star_1 = Review.objects.filter(value = 1).count()
    star_2 = Review.objects.filter(value = 2).count()
    star_3 = Review.objects.filter(value = 3).count()
    star_4 = Review.objects.filter(value = 4).count()
    star_5 = Review.objects.filter(value = 5).count()
    star_all = Review.objects.all().count()
    if (star_all != 0):
        star_avr = (star_1 * 1 + star_2 * 2 + star_3 * 3 + star_4 * 4 + star_5 * 5) / star_all
        return render(request, "reviews.html", {'reviews': reviews, 'star_1': star_1, 'star_2': star_2, 'star_3': star_3, 'star_4': star_4, 'star_5': star_5, 'star_all': star_all, 'star_avr': star_avr, 'form': form})
    else:
        return render(request, "reviews.html", {'reviews': reviews, 'star_1': 0, 'star_2': 0, 'star_3': 0, 'star_4': 0, 'star_5': 0, 'star_all': 0, 'star_avr': 0, 'form': form})

def contacts(request):
    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            number = form.cleaned_data['number']
            hour = form.cleaned_data['hour']
            minute = form.cleaned_data['minute']
            comment = form.cleaned_data['comment']
            
            email_message = f'Имя: {name}.\nНомер телефона: {number}.\nУдобное время: {hour}:{minute}.\nКомментарий: "{comment}".'

            send_mail(
                'Запрос на звонок',
                email_message,
                'starzev.kolechka@gmail.com',  # От кого
                ['maximagapitow@gmail.com'],  # Кому
                fail_silently=False,
            )

            return redirect('/')
    else:
        form = CallForm()
        
    api_key = '828b126c-0067-466a-a2e2-47b4ffa39121'
    address = 'г. Витебск, пр. Фрунзе, 15'
    latitude, longitude = get_coordinates(address, api_key)

    context = {
        'latitude': latitude,
        'longitude': longitude
    }
    return render(request, 'contacts.html', context)

def get_coordinates(address, api_key):
    base_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        'apikey': api_key,
        'geocode': address,
        'format': 'json',
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        json_data = response.json()
        pos = json_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        longitude, latitude = map(float, pos.split())
        return latitude, longitude
    return None, None