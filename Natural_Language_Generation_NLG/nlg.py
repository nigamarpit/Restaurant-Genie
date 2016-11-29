
import sys,json;
sys.path.append('C:\Python27\Lib\site-packages')

Rname=[]
hrateRes=[]
numbers=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine","ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]

from factual import Factual
#factual = Factual('ke8x5LeW6GVnU1aPjTUvJS5Sr12YT2aTA9dDc18r', '4eDL2G2HlRm6ZOTkvxkj2xg86BRgOGUTVLoC5OsF')   #arjun.suresh2708@gmail.com
factual = Factual('O7OPvoeCZbUC3Zsy5qld8zZIuZX99w0SKkT6APy8','V7eHUV01tJUyFqFcaLZrXN8cnIEGbUmdyE1ZO2KB')    #arjun.suresh27@gmail.com

#print("Hello")
#places = factual.table('places')


cuisine="Italian"
postcode="90007"
rating=4   #possible values 1-5
price="expensive"    #possible values Cheap, moderate, Expensive

if(price.lower()=="expensive"):
    price =5
elif(price.lower()=="cheap"):
    price =1

elif(price.lower()=="moderate"):
    price =3


restaurants= factual.table('restaurants-us')
data=restaurants.filters({"$and":[{"cuisine":{"$includes":cuisine}} ,{"rating":rating}     ]}).data()
#print(data)

#data = places.search(cuisine).filters({'postcode':'90007'}).filters({'region':'CA'}).filters({'locality':locality}).data()
#data =hotels.search(cuisine).filters({"$and":[{"locality":{"$eq":"los angeles"}},{"neighborhood":{"$includes":"Downtown"}},{"stars":{"$eq":5}},{"rating":{"$gt":4.0}}]}).data()


def website_not_found(json):
    try:
        return str(json['website'])
    except KeyError:
        return "Nil"


def telephone_not_found(json):
    try:
        return str(json['tel'])
    except KeyError:
        return "Nil"


def rating_not_found(json):
    try:
        return int(json['rating'])
    except KeyError:
        return 0

def price_not_found(json):
    try:
        return int(json['price'])
    except KeyError:
        return 0

def sort_based_on_rating(data):
    data_sorted_on_rating = json.dumps(sorted(data, key=rating_not_found, reverse=True))
    data_sorted_on_rating = json.dumps(sorted(data, key=rating_not_found, reverse=True))

    return data_sorted_on_rating


def nlg(data,cuisine,locality, rating, price):

    if(len(data)>0 and rating>3 and price==1):
        #print(data)

        count_high_rated_res=0
        count_cheap_res=0

        print("I found " + str(len(data)) + " restuarant that serve " + cuisine + " food "     "near " + locality + ".",end=" ")

        #print(data)

        ########Find restaurants based on rating high to low 5 to 0########

        data_sorted_on_rating=sort_based_on_rating(data)    #calling the method

        j_data_sorted_on_rating=json.loads(data_sorted_on_rating)
        #print(data_sorted_on_rating)

        for restaurant in j_data_sorted_on_rating:
            if( 'rating' in restaurant and  restaurant['rating'] >=4 ):
                hrateRes.append(restaurant['name'] +"   Website: "+website_not_found(restaurant) +"     Tel: "+telephone_not_found(restaurant) )
                count_high_rated_res+=1
            else:
                Rname.append(restaurant['name'] + "   Website: " + website_not_found(restaurant) + "     Tel: " + telephone_not_found(restaurant))

        if(count_high_rated_res>=1 and len(data)!=count_high_rated_res):    #If the system found only one highly rated restaurant
            print("Out of which "+str(count_high_rated_res)+" of them are highly rated",end=" ")


        if(count_high_rated_res>1 and len(data)==count_high_rated_res): #If the system found more than one highly rated restaurant
            print("All are highly rated",end=" ")

        #print("highly rated restaurant count is: "+str(count_high_rated_res))


        #######Find restaurants based on rating ends#########



        #########Find restaurants based on price range 1: -$15 2: $15-30 3: $30-50 4: $50-75 5: $75+ #######

        data_sorted_on_price = json.dumps(sorted(data, key=price_not_found))
        j_data_sorted_on_price = json.loads(data_sorted_on_price)

        for restaurant in j_data_sorted_on_price:
            if('price' in restaurant and restaurant['price'] ==1):
                count_cheap_res+=1
        #print(count_cheap_res)

        if(count_cheap_res==0):
            print("and I couldn't find any cheap restaurants in your locality")

        elif(count_cheap_res==1):
            print("and it is cheap with price range of $15 per person. ")

        elif(count_cheap_res>1 and len(data) ==count_cheap_res):
            print("and all of them are cheap with price range of $15 per person. ")

        else:
            print("and " + str(count_cheap_res) + " of them are cheap with price range of $15 per person. ")


        ###########Prints the most preferred restaurants based on rating ############

        if(len(hrateRes)>0):        #Print only if the list is available

            print("The most preferred restaurants based on rating are:")

            for i in range(len(hrateRes))[:3]:
                print(str(i+1)+"."+str(hrateRes[i]))


        ##############Prints just the restaurant list#################Note this is not based on rating, this is just on selection

        if(len(Rname) > 0 and len(hrateRes)==0):

            print("The restaurants based on your preferences are:")

            for i in range(len(Rname))[:3]:
                print(str(i+1)+"."+str(Rname[i]))





    elif(len(data)>0 and rating>3 and price==3):        #case when user wants high rated restaurant and price is moderate(moderate =3)
        print("Moderate")
        count_high_rated_res = 0
        count_moderate_res = 0

        print("I found " + str(len(data)) + " restuarant that serve " + cuisine + " food "     "near " + locality + ".", end=" ")


        ########Find restaurants based on rating high to low 5 to 0########

        data_sorted_on_rating=sort_based_on_rating(data)    #calling the method

        j_data_sorted_on_rating=json.loads(data_sorted_on_rating)
        #print(data_sorted_on_rating)

        for restaurant in j_data_sorted_on_rating:
            if( 'rating' in restaurant and  restaurant['rating'] >=4 ):
                hrateRes.append(restaurant['name'] +"   Website: "+website_not_found(restaurant) +"     Tel: "+telephone_not_found(restaurant) )
                count_high_rated_res+=1
            else:
                Rname.append(restaurant['name'] + "   Website: " + website_not_found(restaurant) + "     Tel: " + telephone_not_found(restaurant))

        if(count_high_rated_res==1):    #If the system found only one highly rated restaurant
            print("Out of which "+str(count_high_rated_res)+" of them is highly rated",end=" ")

        if(count_high_rated_res>1 and count_high_rated_res==len(data)): #If the system found more than one highly rated restaurant
            print("All are highly rated",end=" ")



        #print("highly rated restaurant count is: "+str(count_high_rated_res))


        #######Find restaurants based on rating ends#########











        #########Find restaurants based on price range 1: -$15 2: $15-30 3: $30-50 4: $50-75 5: $75+ #######

        data_sorted_on_price = json.dumps(sorted(data, key=price_not_found))
        j_data_sorted_on_price = json.loads(data_sorted_on_price)

        for restaurant in j_data_sorted_on_price:
            if('price' in restaurant and restaurant['price'] ==3):
                count_moderate_res+=1

        if(count_moderate_res==0):
            print("and I couldn't find any restaurants with moderate pricing in your locality")

        elif(count_moderate_res==1):
            print("and it is moderately priced with approximate price of $30 -50 per person. ")

        elif(count_moderate_res>1 and len(data) ==count_moderate_res):
            print("and all of them are moderately priced with approximate price of $30 -50 per person. ")

        else:
            print("and " + str(count_moderate_res) + " of them are moderately priced with approximate price of $30 -50 per person.")

        if (len(hrateRes) > 0):  # Print only if the list is available

            print("The top restautants based on your rating preferences are:")

            for i in range(len(hrateRes))[:3]:
                print(str(i + 1) + "." + str(hrateRes[i]))



    elif(len(data)>0 and rating>3 and price==5):
        print("Expensive")
        count_high_rated_res = 0
        count_expensive_res = 0

        print("I found " + str(len(data)) + " restuarant that serve " + cuisine + " food "     "near " + locality + ".",
              end=" ")

        ########Find restaurants based on rating high to low 5 to 0########

        data_sorted_on_rating = sort_based_on_rating(data)  # calling the method

        j_data_sorted_on_rating = json.loads(data_sorted_on_rating)
        # print(data_sorted_on_rating)

        for restaurant in j_data_sorted_on_rating:
            if ('rating' in restaurant and restaurant['rating'] >= 4):
                hrateRes.append(restaurant['name'] + "   Website: " + website_not_found(
                    restaurant) + "     Tel: " + telephone_not_found(restaurant))
                count_high_rated_res += 1
            else:
                Rname.append(restaurant['name'] + "   Website: " + website_not_found(
                    restaurant) + "     Tel: " + telephone_not_found(restaurant))

        if (count_high_rated_res == 1):  # If the system found only one highly rated restaurant
            print("Out of which " + str(count_high_rated_res) + " of them is highly rated", end=" ")

        if (count_high_rated_res > 1 and count_high_rated_res == len(
                data)):  # If the system found more than one highly rated restaurant
            print("All are highly rated", end=" ")

        # print("highly rated restaurant count is: "+str(count_high_rated_res))


        #######Find restaurants based on rating ends#########











        #########Find restaurants based on price range 1: -$15 2: $15-30 3: $30-50 4: $50-75 5: $75+ #######

        data_sorted_on_price = json.dumps(sorted(data, key=price_not_found))
        j_data_sorted_on_price = json.loads(data_sorted_on_price)

        for restaurant in j_data_sorted_on_price:
            if ('price' in restaurant and restaurant['price'] == 5):
                count_expensive_res += 1

        if (count_expensive_res == 0):
            print("and I couldn't find any expensive restaurants in your locality")

        elif (count_expensive_res == 1):
            print("and it is moderately priced with approximate price of $75+ per person. ")

        elif (count_expensive_res > 1 and len(data) == count_expensive_res):
            print("and all of them are expensive with approximate price of $75+ per person. ")

        else:
            print("and " + str(count_expensive_res) + " of them are expensive with approximate price of $75+ per person.")

        if (len(hrateRes) > 0):  # Print only if the list is available

            print("The top restautants based on your rating preferences are:")

            for i in range(len(hrateRes))[:3]:
                print(str(i + 1) + "." + str(hrateRes[i]))





    return


def no_results():
    print("I didnt find any such Restaurant in your locality! Please try with other options")
    return

count_found_restaurants=(len(data))
if(count_found_restaurants >0):

    #nlg(Rname,cuisine,data[0]['locality'])
    nlg(data, cuisine, "your locality",rating, price )

elif(count_found_restaurants==0):
    no_results()

