from django.shortcuts import render
import telebot
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        bot = telebot.TeleBot('6309866242:AAH4RsuAPQ07GLklliGTl7JW4mSf46bIuxw')
        bot.send_message(678120082, request.POST.get('message'))
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')

def shopping_cart(request):
    return render(request, 'shopping_cart.html')

def catalog(request):
    return render(request, 'catalog.html')