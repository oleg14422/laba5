from django.shortcuts import render
from pybit.unified_trading import HTTP
from django.http import JsonResponse, HttpResponseServerError, HttpResponse
import json
from .forms import sendTgMessageForm
import telebot
import requests
# Create your views here.

def mainPage(request):
    return render(request, 'mainpage.html')

def diffPage(request):
    symbol = 'BTCUSDT'
    session = HTTP(testnet=False)

    response_s = session.get_tickers(
        category='spot',
        symbol=symbol)

    if response_s['retCode'] !=0:
        raise response_s['retMsg']

    spot_price = float(response_s['result']['list'][0]['lastPrice'])
    response_f = session.get_tickers(
        category='linear',
        symbol=symbol)

    if response_f['retCode'] !=0:
        raise response_f['retMsg']

    f_price = float(response_f['result']['list'][0]['lastPrice'])
    p_diff = spot_price - f_price
    return render(request, 'diffpage.html', {'symbol':symbol, 'spot_price': spot_price, 'f_price': f_price,
                                                                  'p_diff': p_diff, 'diff_': p_diff/spot_price*100})

def getPrice(symbol='BTCUSDT'):
    session = HTTP(testnet=False)

    response_s = session.get_tickers(
        category='spot',
        symbol=symbol)

    if response_s['retCode'] !=0:
        raise response_s['retMsg']

    spot_price = float(response_s['result']['list'][0]['lastPrice'])
    response_f = session.get_tickers(
        category='linear',
        symbol=symbol)

    if response_f['retCode'] != 0:
        raise response_f['retMsg']

    f_price = float(response_f['result']['list'][0]['lastPrice'])
    p_diff = spot_price - f_price

    return p_diff, p_diff / spot_price*100, spot_price, f_price

def getdiffAPI(request):
    result = getPrice()
    json_data = {'symbol': 'BTCUSDT', 'price_diff': result[0], 'diff': result[1], 'spot_price': result[2], 'f_price': result[3]}
    response = JsonResponse(json_data, status = 200)
    return response

def sendMessagePage(request):
    if request.method == 'POST':
        form = sendTgMessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            message = data['message']
            userId = data['userId']


            bot = telebot.TeleBot('6309866242:AAH4RsuAPQ07GLklliGTl7JW4mSf46bIuxw')
            bot.send_message(userId, message)
            context = context = {'form': sendTgMessageForm()}
            return render(request, 'sendMessage.html', context)
        else:
            return HttpResponseServerError('Сталася помилка, форма не валідна')
    context = {'form': sendTgMessageForm()}
    return render(request, 'sendmessage.html', context = context)

def ciscoPage(request):
    return render(request, 'cisco_test.html')

def sitePage(request):
    return HttpResponse(requests.get('https://youtube.com'))