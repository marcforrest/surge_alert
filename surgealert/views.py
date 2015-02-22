from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import Greeting

# Create your views here.
def index(request):
	umhlanga = {'start_latitude':'-29.7275699','start_longitude':'31.0875162'}
	umhlangatop = {'start_latitude':'-29.7098408','start_longitude':'31.0857761'}
	durbanairport = {'start_latitude':'-29.623938','start_longitude':'31.097474'}
	durbannorth = {'start_latitude':'-29.784593','start_longitude':'31.038888'}
	stadium = {'start_latitude':'-29.826097','start_longitude':'31.029597'}
	icccentre = {'start_latitude':'-29.856081','start_longitude':'31.029860'}
	florida = {'start_latitude':'-29.834611','start_longitude':'31.017915'}
	#capetown = {'start_latitude':'-33.903873','start_longitude':'18.417908'}
	

	cities = []
	cities.append(umhlanga)
	cities.append(umhlangatop)
	cities.append(durbanairport)
	cities.append(durbannorth)
	cities.append(stadium)
	cities.append(icccentre)
	cities.append(florida)
	#cities.append(capetown)
	info = ''
	names = ["Umhlanga","Umhlanga Top","Durban Airport","Durban North","Stadium","ICC","Florida Road"]
	#names = ["Durban Airport"]

	for i in cities:
		payload = cities[cities.index(i)]
		headers = {'Authorization':'Token mV8OnocNrS60lQlCmB-VN8PaUOfOjW4svx9SRCM1'}
		r = requests.get('https://api.uber.com/v1/estimates/time', params = payload, headers=headers)
		data = json.loads(r.text)
		info = info + (names[cities.index(i)]) + '    '
		info = info + (data['times'][0]['display_name']) + '    '
		info = info + str((data['times'][0]['estimate'])) + '  <br/><br/>'	
	return HttpResponse(info)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
