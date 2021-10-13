from django.http.response import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.

# import json to load json data to python dictionary
import json

def index(request):
	if request.method == 'POST':
		city = request.POST['city']
		try:
				source=requests.get('https://api.openweathermap.org/data/2.5/weather?q='+ 
				city + '&appid=194c26cd9195c62fbe92d67cf0d386a4').json()
				#print(source)
				data = {
					"location_name":str(source['name']),
					"country_code": str(source['sys']['country']),
					"coordinate": str(source['coord']['lon']) + ' '
								+ str(source['coord']['lat']),
					"temp": str(int(source['main']['temp']-273.15)) + '  °C',
					"pressure": str(source['main']['pressure']),
					"humidity": str(source['main']['humidity']),
				}
				# print(data)
		except Exception as e:
				
				data={
					"location_name":" not valid location",
					"country_code": " ",
					"coordinate":' ',
					"temp":"  ",
					"pressure":'  ',
					"humidity":'  ',
                                                     
				}     		
			


			
	else:
		data ={}
	return render(request, "index.html",data)

