# https://medium.com/free-code-camp/how-to-build-a-web-app-using-pythons-flask-and-google-app-engine-52b1bb82b221
import requests

API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')


def query_api(city):
	try:
		print(API_URL.format(city, API_KEY))
		data = requests.get(API_URL.format(city, API_KEY)).json()
		print (100, data)
	except Exception as exc:
		print(exc)
#	data = None
	return data
