from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import Greeting

# Create your views here.
def index(request):
	durbanairport = {'start_latitude':'-29.623938','start_longitude':'31.097474'}
	

	cities = []
	cities.append(durbanairport)
	info = ''
	names = ["Durban Airport"]

	for i in cities:
		payload = cities[cities.index(i)]
		headers = {'Authorization':'Token mV8OnocNrS60lQlCmB-VN8PaUOfOjW4svx9SRCM1'}
		r = requests.get('https://api.uber.com/v1/estimates/time', params = payload, headers=headers)
		data = json.loads(r.text)
		info = info + (names[cities.index(i)]) + '    '
		info = info + (data['times'][0]['display_name']) + '    '
		info = info + (data['times'][0]['product_id']) + '    '
		info = info + str((data['times'][0]['estimate'])) + '  <br/><br/>'	
	return HttpResponse(info)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
