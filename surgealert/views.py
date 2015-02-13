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
	midwilshire = {'start_latitude':'34.057166','start_longitude':'-118.323956','end_latitude':'34.019479','end_longitude':'-118.401718'}
	downtown = {'start_latitude':'34.042943','start_longitude':'-118.260098','end_latitude':'34.019479','end_longitude':'-118.401718'}
	glendale = {'start_latitude':'34.137907','start_longitude':'-118.250141','end_latitude':'34.019479','end_longitude':'-118.401718'}
	northhollywood = {'start_latitude':'34.161161','start_longitude':'-118.358803','end_latitude':'34.019479','end_longitude':'-118.401718'}

	cities = []
	cities.append(umhlanga)
	cities.append(umhlangatop)
	cities.append(durbanairport)
	cities.append(durbannorth)
	cities.append(midwilshire)
	cities.append(downtown)
	cities.append(glendale)
	cities.append(northhollywood)
	info = ''
	names = ["Umhlanga","Umhlanga Top","Durban Airport","Durban North","Midwilshire","Downtown","Glendale","North Hollywood"]

	for i in cities:
		payload = cities[cities.index(i)]
		headers = {'Authorization':'Token mV8OnocNrS60lQlCmB-VN8PaUOfOjW4svx9SRCM1'}
		r = requests.get('https://api.uber.com/v1/estimates/price', params = payload, headers=headers)
		data = json.loads(r.text)
		info = info + (names[cities.index(i)]) + '    '
		info = info + (data['prices'][0]['display_name']) + '    '
		info = info + str((data['prices'][0]['surge_multiplier'])) + '  <br/><br/>'	
	return HttpResponse(info)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
