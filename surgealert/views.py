from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import Greeting

# Create your views here.
def index(request):
	umhlanga = {'start_latitude':'-29.7275699','start_longitude':'31.0875162','end_latitude':'-29.7254724','end_longitude':'31.0711843'}
	durbanairport = {'start_latitude':'-29.623938','start_longitude':'31.097474','end_latitude':'-29.667131','end_longitude':'31.116346'}
	stadium = {'start_latitude':'-29.826097','start_longitude':'31.029597','end_latitude':'-29.850944','end_longitude':'31.028358'}
	
	cities = []
	cities.append(umhlanga)
	cities.append(durbanairport)
	cities.append(stadium)
	info = ''
	names = ["Umhlanga and Durban North","Airport and Umdloti","Durban Central and Stadium"]
	info = '<?xml version="1.0" encoding="UTF-8" ?> <rss version="2.0"> <channel> <title>Durban Surge</title><link></link>  <description></description>'
	#info2
	
	for i in cities:
		payload = cities[cities.index(i)]
		headers = {'Authorization':'Token OrgGRZYTTVJTUcfQ_LiVFr8vFqRw4feetgE46PAg'}
		r = requests.get('https://api.uber.com/v1/estimates/price', params = payload, headers=headers)
		data = json.loads(r.text)
		info = info + '<item><title>' + (names[cities.index(i)]) + '</title>'
		info = info + '<description>' + (data['prices'][0]['display_name']) + ' - ' 
		info = info + str((data['prices'][0]['surge_multiplier'])) + '</description></item>'	
	return HttpResponse(info + '</channel> </rss>')
	#response = HttpResponse()
	#response.write(info)
	#response.write('</channel> </rss>')
	#print info + '</channel> </rss>'
	

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
