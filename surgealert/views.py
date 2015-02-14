from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import Greeting

# Create your views here.
def index(request):
	umhlanga = {'start_latitude':'-29.7275699','start_longitude':'31.0875162','end_latitude':'-29.7254724','end_longitude':'31.0711843'}
	umhlangatop = {'start_latitude':'-29.7098408','start_longitude':'31.0857761','end_latitude':'-29.7326701','end_longitude':'31.0835223'}
	durbanairport = {'start_latitude':'-29.623938','start_longitude':'31.097474','end_latitude':'-29.667131','end_longitude':'31.116346'}
	durbannorth = {'start_latitude':'-29.784593','start_longitude':'31.038888','end_latitude':'-29.758671','end_longitude':'31.054951'}
	stadium = {'start_latitude':'-29.826097','start_longitude':'31.029597','end_latitude':'-29.850944','end_longitude':'31.028358'}
	icccentre = {'start_latitude':'-29.856081','start_longitude':'31.029860','end_latitude':'-29.870115','end_longitude':'31.046594'}
	florida = {'start_latitude':'-29.834611','start_longitude':'31.017915','end_latitude':'-29.848767','end_longitude':'30.999229'}
	
	

	cities = []
	cities.append(umhlanga)
	cities.append(umhlangatop)
	cities.append(durbanairport)
	cities.append(durbannorth)
	cities.append(stadium)
	cities.append(icccentre)
	cities.append(florida)
	info = ''
	names = ["Umhlanga","Umhlanga Top","Durban Airport","Durban North","Stadium","ICC","Florida Road"]
	info = '<?xml version="1.0" encoding="UTF-8" ?> <rss version="2.0"> <channel> <title>Durban Surge</title><link></link>  <description></description>'
	#info2
	
	for i in cities:
		payload = cities[cities.index(i)]
		headers = {'Authorization':'Token mV8OnocNrS60lQlCmB-VN8PaUOfOjW4svx9SRCM1'}
		r = requests.get('https://api.uber.com/v1/estimates/price', params = payload, headers=headers)
		data = json.loads(r.text)
		info = info + '<item><title>' + (names[cities.index(i)]) + '</title>'
		info = info + '<description>' + (data['prices'][0]['display_name']) + ' - ' 
		info = info + str((data['prices'][0]['surge_multiplier'])) + '</description></item>'	
	return HttpResponse(info)
	#response = HttpResponse()
	#response.write(info)
	#response.write('</channel> </rss>')
	#print info + '</channel> </rss>'
	

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
