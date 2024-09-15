city_flights = input("Enter the  name of the city you will be flying to (Cape Town, East London or Durban) ")
num_nights = int(input("Enter the number of nights you'll stay at hotel "))
rental_days = int(input("Enter the number of days you will hiring a car "))


def hotel_cost(num_nights):
    total = num_nights * 500
    return(total)


def plane_cost(city_flight):
    if city_flight == "Durban":
        return(700)
    elif city_flight == "Cape Town":
        return(900)
    elif city_flight == "East London":
        return(800)

def car_rental(rental_days):
    total = rental_days * 600
    return(total)

def holiday_cost (h_cost,p_cost, c_rental):
    hotel_total = hotel_cost(h_cost)
    print("hotel total for " + str(h_cost) + " days at a rate of 500 per day is " + str(hotel_total))
    
    
    plane_total = plane_cost(p_cost)
    print("plane total for " + str(p_cost) + " is "+ str(plane_total))
    
    
    car_total = car_rental(c_rental)
    print("car total for " + str(c_rental) + " days at a rate of 600 per day is " + str(car_total))
    
    holiday_total = (int(hotel_total) + int(plane_total) + int(car_total))
    print("holiday total " + str(holiday_total))
    
holiday_cost(num_nights, city_flights, rental_days)
   
    
    

 



    
    

                                                                                                                                                                                                  
  
    
    
   




    