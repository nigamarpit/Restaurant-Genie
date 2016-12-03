'''
Created on 14-Nov-2016

@author: mac
'''
from factual import Factual
import json
import requests
from factual.utils import circle
import NLU
import nlg
import SpeechGeneration as SG
import SpeechSynthesis as SS

#speak = wincl.Dispatch("SAPI.SpVoice")

#speak.Speak("I found following restaurants near you!")
#speak.Speak("I found 20 restuarant that serve Italian food near your locality. Out of which 13 are highly rated and 6 of them are cheap with price range of $15 per person.")
#speak.Speak("The most preferred restaurants based on rating are:")

cuisine="empty"
cuisine_status="empty"
price="empty"
price_status = "empty"
location="empty"
location_status="empty"
rating="empty"
rating_status="empty"

def invokeNLGGreeting():
	SG.SpeechOutput("Hello, how may I help you today?")
	inp=SS.microphoneListen()
	#print(inp)
	status=extractInfoFromNLU(inp)
	while(status==-1):
		status=requestStatementOnError()
	return 0

def extractInfoFromNLU(inp):
	global cuisine
	global price
	global rating
	global location
	global cuisine_status
	global location_status
	global price_status
	global rating_status

	provideInfoDM=NLU.parseInput(inp)
	#print(provideInfoDM)
	if('status' in provideInfoDM):
		return -1
	if('cuisine' in provideInfoDM):
		cuisine=provideInfoDM['cuisine']
		cuisine_status=confirm_cuisine()	
	elif('location' in provideInfoDM):
		location=provideInfoDM['location']
		location_status=confirm_location()
	elif('price' in provideInfoDM):
		price=provideInfoDM['price']
		if(price == "dnc"):
			pass
		else:
			price_status = confirm_price()
	elif('rating' in provideInfoDM):
		rating=provideInfoDM['rating']
		if(rating =="dnc"):
			pass
		else:
			rating_status = confirm_rating()
	return 0

def get_cuisine_nlu(cuisineFromNLU):
	global cuisine
	cuisine=cuisineFromNLU
	confirm_cuisine()

def request_cuisine():
	global cusine
	cuisine = request_cuisine_util()
	while (cuisine=="empty" or cuisine ==""):
		cuisine = request_cuisine_util() 
	
	return cuisine

def request_cuisine_util():
	global cuisine
	SG.SpeechOutput("Please enter your preference for cuisine")
	cuisine = input()

	return cuisine

def confirm_cuisine_util():
	global cuisine_status
	s='You asked for '+cuisine+' cuisine. Is that correct?'
	SG.SpeechOutput(s)
	inp=SS.microphoneListen()
	cuisine_status = inp
	if cuisine_status.lower() in ['yes','y','ya','yeah']:
		return "filled"
	return cuisine_status       

def confirm_cuisine():
	global cusine_status
	cuisine_status = confirm_cuisine_util()
	while (cuisine_status!="filled"):
		cuisine = "empty"
		cuisine_status = "empty"
		cusine = request_cuisine()
		cuisine_status = confirm_cuisine_util()
		if(cuisine_status =="filled"):
			break
		
	return cuisine_status
 
def request_location():
	global location
	location = request_location_util()
	while (location=="empty" or location ==""):
		location = request_location_util()	
	return location

def request_location_util():
	global location
	s="Please enter your preference for location"
	SG.SpeechOutput(s)
	inp=SS.microphoneListen()
	location = inp
	return location

def confirm_location_util():
	global location_status
	SG.SpeechOutput("Confirm your location preference - "+location)
	inp=SS.microphoneListen()
	location_status = inp

	if(location_status.lower() in ['yes','y','ya','yeah']):
		return "filled"
	return location_status       

def confirm_location():
	global location_status
	location_status = confirm_location_util()
	while (location_status!="filled"):
		location = "empty"
		location_status = "empty"
		location = request_location()
		location_status = confirm_location_util()
		if(location_status =="filled"):
			break
		
	return location_status
 
def request_price():
	global price
	price = request_price_util()
	while (price=="empty" or price ==""):
		price= request_price_util() 
	
	return price

def request_price_util():
	global price
	SG.SpeechOutput("Please enter your preference for price [Cheap/Moderate/Expensive]")
	inp=SS.microphoneListen()
	price = inp
	return price

def confirm_price_util():
	global price_status
	s="You entered "+price+". Is that correct?"
	SG.SpeechOutput(s)
	inp=SS.microphoneListen()
	price_status = inp

	if(price_status.lower() in ['yes','y','ya','yeah']):
		return "filled"
	if(price_status=="dont't care"):
		return "dnc"
	return price_status       

def confirm_price():
	global price_status
	price_status = confirm_price_util()
	while (price_status!="filled" and  price_status!="dnc"):
		price = "empty"
		price_status = "empty"
		price = request_price()
		price_status = confirm_price_util()
		if(price_status =="filled"):
			break
		
	return price_status

def request_rating():
	global rating
	rating = request_rating_util()
	while (rating=="empty" or rating ==""):
		rating= request_rating_util() 	
	return rating

def request_rating_util():
	d={'one':'1','two':'2','three':'3','four':'4','five':'5'}
	global rating
	s="Please enter your preference for rating [1 - 5]"
	SG.SpeechOutput(s)
	inp=SS.microphoneListen()
	rating = d[inp.lower()]
	return rating

def confirm_rating_util():
	global rating_status
	if(rating==-1):
		SG.SpeechOutput("Do you want me to choose a rating?")
		rating_status = input()
	else:
		SG.SpeechOutput("You entered " +str(rating)+". Is that correct?")
		inp=SS.microphoneListen()
		rating_status = inp

	if(rating_status.lower() in ['yes','y','ya','yeah']):
		return "filled"
	if(rating_status=="dnc"):
		return "dnc"
	return rating_status       

def confirm_rating():
	global rating_status
	rating_status = confirm_rating_util()
	while (rating_status!="filled" and rating_status !="dnc"):
		rating= "empty"
		rating_status = "empty"
		rating = request_rating()
		rating_status = confirm_rating_util()
		if(rating_status =="filled"):
			break
		
	return rating_status

def queryAPI(cuisine,location,price,rating):
	your_key = "IFEtuFdchgMa7GUu8X9BFTMtJDJ7XaEGlLpbdZb1"
	your_secret = "0ZBLOnq5Fk0QspMeAqP5t0IvqTsb8mZtGvFSHU3a"
	factual = Factual(your_key, your_secret)
	#data={}
	
	places = factual.table('restaurants-us')
	if(price =='dnc' and rating==-1):
		#input('here1')	
		data = places.filters({'$and':[
								   {'locality':{'$eq':location}},
								   {'cuisine':{'$eq':cuisine}}
								   ]}).data()
	elif(price == 'dnc'):
		#input('here2')
		data = places.filters({'$and':[
								   {'locality':{'$eq':location}},
								   {'cuisine':{'$eq':cuisine}} ,
								   {'rating':{'$eq':rating}}
								   ]}).data()
	elif(rating==-1):
		#input('here3')
		data = places.filters({'$and':[
								   {'locality':{'$eq':location}},
								  {'cuisine':{'$eq':cuisine}},
								   {'price':price}
								   ]}).data()
	elif location is None:
		#input('here4')
		data = places.filters({'$and':[
								   {'locality':{'$eq':location}},
								  {'cuisine':{'$eq':cuisine}},
								   {'price':price},
								   {'rating':rating}
								   ]}).data()
	else:
		send_url = 'http://freegeoip.net/json'
		r = requests.get(send_url)
		j = json.loads(r.text)
		lat = j['latitude']
		lon = j['longitude']
		data = places.filters({'$and':[
								  {'cuisine':{'$eq':cuisine}},
								   {'price':price},
								   {'rating':rating}
								   ]}).geo({'$circle':{'$center':[lat, lon],'$meters': 2500}}).data()
		#print('here5')
	#input(data)
		#http://api.v3.factual.com/t/places/facets?select=category_ids&geo={"$circle":{"$center":[34.06018, -118.41835],"$meters": 5000}}

	nlg.nlg(data, cuisine, location,rating, price)

	with open("finalresult.txt", "w",encoding="latin1") as outfile:
		json.dump(data, outfile, indent=4)

def requestCuisineOnError():

	
	SG.SpeechOutput("I didn't understand. Could you please tell me your cuisine preference again?")
	inp=SS.microphoneListen()
	cuisineInput=inp
	return extractInfoFromNLU(cuisineInput)

def requestLocationOnError():
	SG.SpeechOutput("I didn't understand. Could you please tell me your location preference again?")
	inp=SS.microphoneListen()
	cuisineInput=inp

	return extractInfoFromNLU(cuisineInput)

def requestPriceOnError():
	SG.SpeechOutput("I didn't understand. Could you please tell me your price preference again from Cheap Expensive Moderate")
	inp=SS.microphoneListen()
	cuisineInput=inp

	return extractInfoFromNLU(cuisineInput)

def requestRatingOnError():
	SG.SpeechOutput("I didn't understand. Could you please tell me your rating preference again? [1 - 5]")
	inp=SS.microphoneListen()
	cuisineInput=inp
	return extractInfoFromNLU(cuisineInput)

def requestStatementOnError():
	SG.SpeechOutput("I didn't understand. Could you please repeat again?")
	statementInput=input()
	return extractInfoFromNLU(statementInput)
	
if __name__ == "__main__":

	invokeNLGGreeting()
	status=0
	if(cuisine=="empty"):
		SG.SpeechOutput("Please enter your preference for cuisine")
		inp=SS.microphoneListen()
		cuisineInput=inp
	
		status=extractInfoFromNLU(cuisineInput)
		while(status==-1):
			status=requestCuisineOnError()
		#cuisine_status = confirm_cuisine()

	if(location=="empty"):
		s="Do you have any location preference?"
		SG.SpeechOutput(s)
		inp=SS.microphoneListen()
		bool_location=inp
		if bool_location.lower() in ['yes','y','ya','yeah']:
			s="Please provide your preference for location"
			SG.SpeechOutput(s)
			inp=SS.microphoneListen()
			locationInput=inp
			status=extractInfoFromNLU(locationInput)
			while(status==-1):
				status=requestLocationOnError()
		#location_status = confirm_location()

	if(price=="empty"):
		s="Please enter your preference for price from Cheap, Moderate, Expensive"
		SG.SpeechOutput(s)
		inp=SS.microphoneListen()
		priceInput=inp
		status=extractInfoFromNLU(priceInput)
		while(status==-1):
			status=requestPriceOnError()


	if(rating=="empty"):
		d={'one':'1','two':'2','three':'3','four':'4','five':'5'}
		s="Please enter your preference for rating [1 - 5]"
		SG.SpeechOutput(s)
		inp=SS.microphoneListen()
		ratingInput=d[inp.lower()]
		status=extractInfoFromNLU(ratingInput)
		while(status==-1):
			status=requestRatingOnError()

	 
	'''print(cuisine)
	print(cuisine_status)
	 
	print(location)
	print(location_status)  
	 
	print(price)
	print(price_status)
	 
	 
	print(rating)
	print(rating_status)'''


	if(price.lower()=="expensive"):
		price=5
	elif(price.lower()=="cheap"):
		price=1
	elif(price.lower()=="moderate"):
		price=3

	queryAPI(cuisine,location,price,rating)