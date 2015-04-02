from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import Greeting

# Create your views here.
def index(request):
	airport = {'start_latitude':'-26.1291975','start_longitude':'28.2405777','end_latitude':'-26.133945','end_longitude':'28.2396804'}
	Sandton = {'start_latitude':'-26.1313443','start_longitude':'28.1041001','end_latitude':'-26.1228039','end_longitude':'27.9625699'}
	EllisPark = {'start_latitude':'-26.2004482','start_longitude':'28.0510613','end_latitude':'-26.2013242','end_longitude':'28.0459114'}
	Midrand = {'start_latitude':'-26.0053635','start_longitude':'28.1036319','end_latitude':'-25.9879091','end_longitude':'28.1256145'}
	
	cities = []
	cities.append(airport)
	cities.append(Sandton)
	cities.append(EllisPark)
	cities.append(Midrand)

	info = ''
	names = ["Airport","Sandton","EllisPark","Midrand"]
	info = '<?xml version="1.0" encoding="UTF-8" ?> <rss version="2.0"> <channel> <title>Joburg Surge</title><link></link>  <description></description>'
	
	for i in cities:
		payload = cities[cities.index(i)]
		headers = {'Authorization':'Token lLH8AXcPuzyGXocg6e4uXB37TYeandwplaomCnX3'}
		r = requests.get('https://api.uber.com/v1/estimates/price', params = payload, headers=headers)
		data = json.loads(r.text)
		info = info + '<item><title>' + (names[cities.index(i)]) + '</title>'
		info = info + '<description>' + (data['prices'][1]['display_name']) + ' - ' 
		info = info + str((data['prices'][1]['surge_multiplier'])) + '</description></item>'	
	return HttpResponse(info + '</channel> </rss>')	



def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
